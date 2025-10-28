from fastapi import APIRouter, UploadFile, File, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from pydantic import BaseModel, EmailStr
from typing import List, Optional
import logging
import os
import json
from datetime import datetime

from app.database import get_db
from app.models.resume import Resume
from app.models.user import User
from app.utils.security import decode_token
from app.services.resume_parser import parse_pdf, parse_docx, extract_resume_data
from app.config import settings

logger = logging.getLogger(__name__)
router = APIRouter()
security = HTTPBearer()

class ResumeData(BaseModel):
    full_name: str
    email: EmailStr
    phone: Optional[str] = None
    summary: Optional[str] = None
    skills: List[str] = []
    experience: List[str] = []
    education: List[str] = []

class ResumeResponse(BaseModel):
    id: int
    title: str
    full_name: str
    email: str
    phone: Optional[str]
    skills: List[str]
    ats_score: float
    created_at: datetime

class ATSScoreResponse(BaseModel):
    score: float
    strengths: List[str]
    improvements: List[str]
    keyword_matches: int
    total_keywords: int

async def get_current_user_id(credentials: HTTPAuthCredentials = Depends(security)) -> int:
    """Extract user ID from JWT token"""
    token = credentials.credentials
    payload = decode_token(token)
    
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )
    
    return int(payload.get("sub"))

@router.post("/upload")
async def upload_resume(
    file: UploadFile = File(...),
    credentials: HTTPAuthCredentials = Depends(security),
    db: AsyncSession = Depends(get_db)
):
    """Upload and parse resume file"""
    try:
        user_id = await get_current_user_id(credentials)
        
        # Validate file type
        allowed_extensions = {".pdf", ".docx", ".doc"}
        file_ext = os.path.splitext(file.filename)[1].lower()
        
        if file_ext not in allowed_extensions:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Only PDF and DOCX files are allowed"
            )
        
        # Create upload directory if it doesn't exist
        os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
        
        # Save file
        file_path = os.path.join(settings.UPLOAD_DIR, f"{user_id}_{datetime.utcnow().timestamp()}_{file.filename}")
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)
        
        # Parse resume based on file type
        if file_ext == ".pdf":
            parse_result = parse_pdf(file_path)
        else:
            parse_result = parse_docx(file_path)
        
        if "error" in parse_result:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error parsing file: {parse_result['error']}"
            )
        
        # Extract structured data
        resume_data = extract_resume_data(parse_result["text"])
        
        # Create resume record
        new_resume = Resume(
            user_id=user_id,
            title=file.filename.replace(file_ext, ""),
            full_name=resume_data["full_name"],
            email=resume_data["email"],
            phone=resume_data["phone"],
            skills=json.dumps(resume_data["skills"]),
            experience=json.dumps(resume_data["experience"]),
            education=json.dumps(resume_data["education"]),
            file_path=file_path
        )
        
        db.add(new_resume)
        await db.commit()
        await db.refresh(new_resume)
        
        logger.info(f"Resume uploaded successfully for user {user_id}")
        
        return {
            "id": new_resume.id,
            "title": new_resume.title,
            "full_name": new_resume.full_name,
            "email": new_resume.email,
            "phone": new_resume.phone,
            "skills": resume_data["skills"],
            "message": "Resume uploaded and parsed successfully"
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Resume upload error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error uploading resume"
        )

@router.get("/list")
async def list_resumes(
    credentials: HTTPAuthCredentials = Depends(security),
    db: AsyncSession = Depends(get_db)
):
    """Get all resumes for current user"""
    try:
        user_id = await get_current_user_id(credentials)
        
        result = await db.execute(
            select(Resume).where(Resume.user_id == user_id).order_by(Resume.created_at.desc())
        )
        resumes = result.scalars().all()
        
        return [
            {
                "id": r.id,
                "title": r.title,
                "full_name": r.full_name,
                "email": r.email,
                "ats_score": r.ats_score,
                "created_at": r.created_at
            }
            for r in resumes
        ]
    except Exception as e:
        logger.error(f"Error listing resumes: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving resumes"
        )

@router.get("/{resume_id}")
async def get_resume(
    resume_id: int,
    credentials: HTTPAuthCredentials = Depends(security),
    db: AsyncSession = Depends(get_db)
):
    """Get specific resume details"""
    try:
        user_id = await get_current_user_id(credentials)
        
        result = await db.execute(
            select(Resume).where((Resume.id == resume_id) & (Resume.user_id == user_id))
        )
        resume = result.scalar_one_or_none()
        
        if not resume:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Resume not found"
            )
        
        return {
            "id": resume.id,
            "title": resume.title,
            "full_name": resume.full_name,
            "email": resume.email,
            "phone": resume.phone,
            "summary": resume.summary,
            "skills": json.loads(resume.skills) if resume.skills else [],
            "experience": json.loads(resume.experience) if resume.experience else [],
            "education": json.loads(resume.education) if resume.education else [],
            "ats_score": resume.ats_score,
            "created_at": resume.created_at
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error retrieving resume: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving resume"
        )

@router.post("/analyze-ats/{resume_id}", response_model=ATSScoreResponse)
async def analyze_ats(
    resume_id: int,
    job_description: str,
    credentials: HTTPAuthCredentials = Depends(security),
    db: AsyncSession = Depends(get_db)
):
    """Analyze resume for ATS compatibility"""
    try:
        user_id = await get_current_user_id(credentials)
        
        result = await db.execute(
            select(Resume).where((Resume.id == resume_id) & (Resume.user_id == user_id))
        )
        resume = result.scalar_one_or_none()
        
        if not resume:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Resume not found"
            )
        
        # Extract keywords from job description
        job_keywords = set(job_description.lower().split())
        resume_text = f"{resume.full_name} {resume.email} {resume.phone} {resume.summary} {resume.skills}".lower()
        resume_keywords = set(resume_text.split())
        
        # Calculate matches
        matches = job_keywords.intersection(resume_keywords)
        match_percentage = (len(matches) / len(job_keywords) * 100) if job_keywords else 0
        
        # Generate score (0-100)
        score = min(100, match_percentage * 1.5)
        
        # Determine strengths and improvements
        strengths = []
        improvements = []
        
        if score >= 70:
            strengths.append("Good keyword match with job description")
        else:
            improvements.append("Add more relevant keywords from job description")
        
        if resume.skills:
            strengths.append("Skills section is present")
        else:
            improvements.append("Add a skills section")
        
        if resume.phone and resume.email:
            strengths.append("Contact information is complete")
        else:
            improvements.append("Ensure all contact information is present")
        
        # Update resume ATS score
        resume.ats_score = score
        await db.commit()
        
        logger.info(f"ATS analysis completed for resume {resume_id}")
        
        return ATSScoreResponse(
            score=round(score, 2),
            strengths=strengths,
            improvements=improvements,
            keyword_matches=len(matches),
            total_keywords=len(job_keywords)
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"ATS analysis error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error analyzing resume"
        )

@router.delete("/{resume_id}")
async def delete_resume(
    resume_id: int,
    credentials: HTTPAuthCredentials = Depends(security),
    db: AsyncSession = Depends(get_db)
):
    """Delete a resume"""
    try:
        user_id = await get_current_user_id(credentials)
        
        result = await db.execute(
            select(Resume).where((Resume.id == resume_id) & (Resume.user_id == user_id))
        )
        resume = result.scalar_one_or_none()
        
        if not resume:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Resume not found"
            )
        
        # Delete file
        if resume.file_path and os.path.exists(resume.file_path):
            os.remove(resume.file_path)
        
        await db.delete(resume)
        await db.commit()
        
        logger.info(f"Resume {resume_id} deleted")
        
        return {"message": "Resume deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error deleting resume: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error deleting resume"
        )

@router.get("/templates")
async def get_templates():
    """Get available resume templates"""
    return {
        "templates": [
            {"id": 1, "name": "Professional", "description": "Clean and professional design"},
            {"id": 2, "name": "Modern", "description": "Contemporary layout with accent colors"},
            {"id": 3, "name": "Minimal", "description": "Simple and elegant design"}
        ]
    }
