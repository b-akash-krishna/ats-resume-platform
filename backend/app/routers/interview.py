from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import logging
import json

from app.database import get_db
from app.models.interview import Interview, InterviewQuestion, InterviewResponse
from app.utils.security import decode_token
from app.services.question_generator import generate_interview_questions
from app.services.response_analyzer import analyze_response

logger = logging.getLogger(__name__)
router = APIRouter()
security = HTTPBearer()

class InterviewSetupRequest(BaseModel):
    job_title: str
    job_description: str
    difficulty: str = "medium"

class QuestionResponse(BaseModel):
    id: int
    question_number: int
    question: str
    category: str

class SubmitResponseRequest(BaseModel):
    question_id: int
    answer: str
    duration: int

class ResponseAnalysisResponse(BaseModel):
    score: float
    feedback: str
    quality_metrics: dict

class InterviewReportResponse(BaseModel):
    overall_score: float
    communication_score: float
    technical_score: float
    duration: int
    strengths: List[str]
    improvements: List[str]

async def get_current_user_id(credentials: HTTPAuthorizationCredentials = Depends(security)) -> int:
    """Extract user ID from JWT token"""
    token = credentials.credentials
    payload = decode_token(token)
    
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )
    
    return int(payload.get("sub"))

@router.post("/setup")
async def setup_interview(
    request: InterviewSetupRequest,
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: AsyncSession = Depends(get_db)
):
    """Setup mock interview session"""
    try:
        user_id = await get_current_user_id(credentials)
        
        # Generate questions based on job description
        questions_data = generate_interview_questions(
            job_description=request.job_description,
            job_title=request.job_title,
            difficulty=request.difficulty,
            count=5
        )
        
        # Create interview record
        new_interview = Interview(
            user_id=user_id,
            job_title=request.job_title,
            job_description=request.job_description,
            difficulty=request.difficulty,
            status="in_progress"
        )
        
        db.add(new_interview)
        await db.flush()
        
        # Create interview questions
        for idx, q_data in enumerate(questions_data, 1):
            question = InterviewQuestion(
                interview_id=new_interview.id,
                question_number=idx,
                question=q_data["question"],
                category=q_data["category"]
            )
            db.add(question)
        
        await db.commit()
        await db.refresh(new_interview)
        
        logger.info(f"Interview setup completed for user {user_id}: {request.job_title}")
        
        return {
            "interview_id": new_interview.id,
            "job_title": new_interview.job_title,
            "difficulty": new_interview.difficulty,
            "total_questions": len(questions_data),
            "message": "Interview session created successfully"
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Interview setup error: {str(e)}")
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error setting up interview"
        )

@router.get("/questions/{interview_id}", response_model=List[QuestionResponse])
async def get_interview_questions(
    interview_id: int,
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: AsyncSession = Depends(get_db)
):
    """Get questions for an interview session"""
    try:
        user_id = await get_current_user_id(credentials)
        
        # Verify interview belongs to user
        result = await db.execute(
            select(Interview).where(
                (Interview.id == interview_id) & (Interview.user_id == user_id)
            )
        )
        interview = result.scalar_one_or_none()
        
        if not interview:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Interview not found"
            )
        
        # Get questions
        result = await db.execute(
            select(InterviewQuestion).where(
                InterviewQuestion.interview_id == interview_id
            ).order_by(InterviewQuestion.question_number)
        )
        questions = result.scalars().all()
        
        return [
            QuestionResponse(
                id=q.id,
                question_number=q.question_number,
                question=q.question,
                category=q.category
            )
            for q in questions
        ]
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching questions: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving questions"
        )

@router.post("/submit-response/{interview_id}/{question_id}", response_model=ResponseAnalysisResponse)
async def submit_response(
    interview_id: int,
    question_id: int,
    request: SubmitResponseRequest,
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: AsyncSession = Depends(get_db)
):
    """Submit and analyze interview response"""
    try:
        user_id = await get_current_user_id(credentials)
        
        # Verify interview belongs to user
        result = await db.execute(
            select(Interview).where(
                (Interview.id == interview_id) & (Interview.user_id == user_id)
            )
        )
        interview = result.scalar_one_or_none()
        
        if not interview:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Interview not found"
            )
        
        # Get question
        result = await db.execute(
            select(InterviewQuestion).where(InterviewQuestion.id == question_id)
        )
        question = result.scalar_one_or_none()
        
        if not question:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Question not found"
            )
        
        # Analyze response
        analysis = analyze_response(
            question=question.question,
            answer=request.answer,
            category=question.category,
            difficulty=interview.difficulty
        )
        
        # Save response
        new_response = InterviewResponse(
            interview_id=interview_id,
            question_id=question_id,
            answer=request.answer,
            duration=request.duration,
            score=analysis["score"],
            feedback=analysis["feedback"]
        )
        
        db.add(new_response)
        await db.commit()
        
        logger.info(f"Response submitted for interview {interview_id}, question {question_id}")
        
        return ResponseAnalysisResponse(
            score=analysis["score"],
            feedback=analysis["feedback"],
            quality_metrics=analysis["quality_metrics"]
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error submitting response: {str(e)}")
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error submitting response"
        )

@router.post("/complete/{interview_id}")
async def complete_interview(
    interview_id: int,
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: AsyncSession = Depends(get_db)
):
    """Complete interview and generate report"""
    try:
        user_id = await get_current_user_id(credentials)
        
        # Get interview
        result = await db.execute(
            select(Interview).where(
                (Interview.id == interview_id) & (Interview.user_id == user_id)
            )
        )
        interview = result.scalar_one_or_none()
        
        if not interview:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Interview not found"
            )
        
        # Get all responses
        result = await db.execute(
            select(InterviewResponse).where(InterviewResponse.interview_id == interview_id)
        )
        responses = result.scalars().all()
        
        if not responses:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No responses submitted"
            )
        
        # Calculate scores
        scores = [r.score for r in responses]
        overall_score = sum(scores) / len(scores) if scores else 0
        
        # Categorize scores
        communication_responses = [r for r in responses if r.question.category == "behavioral"]
        technical_responses = [r for r in responses if r.question.category == "technical"]
        
        communication_score = (
            sum(r.score for r in communication_responses) / len(communication_responses)
            if communication_responses else overall_score
        )
        technical_score = (
            sum(r.score for r in technical_responses) / len(technical_responses)
            if technical_responses else overall_score
        )
        
        # Calculate total duration
        total_duration = sum(r.duration for r in responses)
        
        # Update interview
        interview.overall_score = overall_score
        interview.communication_score = communication_score
        interview.technical_score = technical_score
        interview.duration = total_duration
        interview.status = "completed"
        interview.updated_at = datetime.utcnow()
        
        await db.commit()
        
        logger.info(f"Interview {interview_id} completed with score {overall_score:.2f}")
        
        return {
            "interview_id": interview_id,
            "overall_score": round(overall_score, 2),
            "communication_score": round(communication_score, 2),
            "technical_score": round(technical_score, 2),
            "duration": total_duration,
            "status": "completed",
            "message": "Interview completed successfully"
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error completing interview: {str(e)}")
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error completing interview"
        )

@router.get("/report/{interview_id}", response_model=InterviewReportResponse)
async def get_interview_report(
    interview_id: int,
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: AsyncSession = Depends(get_db)
):
    """Get interview report"""
    try:
        user_id = await get_current_user_id(credentials)
        
        # Get interview
        result = await db.execute(
            select(Interview).where(
                (Interview.id == interview_id) & (Interview.user_id == user_id)
            )
        )
        interview = result.scalar_one_or_none()
        
        if not interview:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Interview not found"
            )
        
        # Get responses for feedback
        result = await db.execute(
            select(InterviewResponse).where(InterviewResponse.interview_id == interview_id)
        )
        responses = result.scalars().all()
        
        # Generate strengths and improvements
        strengths = []
        improvements = []
        
        if interview.overall_score >= 80:
            strengths.append("Excellent overall performance")
        if interview.communication_score >= 75:
            strengths.append("Strong communication skills")
        if interview.technical_score >= 75:
            strengths.append("Solid technical knowledge")
        
        if interview.overall_score < 70:
            improvements.append("Focus on providing more detailed answers")
        if interview.communication_score < 70:
            improvements.append("Work on articulating your thoughts more clearly")
        if interview.technical_score < 70:
            improvements.append("Deepen your technical knowledge in key areas")
        
        if not strengths:
            strengths.append("Good effort on the interview")
        if not improvements:
            improvements.append("Continue practicing to maintain performance")
        
        return InterviewReportResponse(
            overall_score=round(interview.overall_score, 2),
            communication_score=round(interview.communication_score, 2),
            technical_score=round(interview.technical_score, 2),
            duration=interview.duration,
            strengths=strengths,
            improvements=improvements
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error retrieving report: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving report"
        )

@router.get("/list")
async def list_interviews(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: AsyncSession = Depends(get_db)
):
    """Get all interviews for current user"""
    try:
        user_id = await get_current_user_id(credentials)
        
        result = await db.execute(
            select(Interview).where(Interview.user_id == user_id).order_by(Interview.created_at.desc())
        )
        interviews = result.scalars().all()
        
        return [
            {
                "id": i.id,
                "job_title": i.job_title,
                "difficulty": i.difficulty,
                "overall_score": i.overall_score,
                "status": i.status,
                "created_at": i.created_at
            }
            for i in interviews
        ]
    except Exception as e:
        logger.error(f"Error listing interviews: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving interviews"
        )
