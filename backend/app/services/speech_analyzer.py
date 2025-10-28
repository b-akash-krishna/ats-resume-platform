import logging
from typing import Dict, Any
from app.services.llm_service import generate_text

logger = logging.getLogger(__name__)

async def transcribe_audio(audio_file_path: str) -> str:
    """
    Transcribe audio file using Whisper
    """
    try:
        import whisper
        model = whisper.load_model("base")
        result = model.transcribe(audio_file_path)
        transcription = result["text"]
        logger.info(f"Successfully transcribed audio: {audio_file_path}")
        return transcription
    except Exception as e:
        logger.error(f"Error transcribing audio: {e}")
        return ""

async def analyze_response(
    question: str,
    answer: str,
    job_description: str
) -> Dict[str, Any]:
    """
    Analyze interview response for quality and relevance
    """
    try:
        prompt = f"""Analyze this interview response and provide feedback.

Question: {question}

Candidate's Answer: {answer}

Job Requirements: {job_description}

Provide analysis in the following format:
SCORE: (0-100)
STRENGTHS:
- Point 1
- Point 2
IMPROVEMENTS:
- Point 1
- Point 2
FEEDBACK: Brief overall feedback"""
        
        response = await generate_text(prompt)
        analysis = parse_analysis_response(response)
        
        logger.info(f"Analyzed interview response with score: {analysis['score']}")
        return analysis
    except Exception as e:
        logger.error(f"Error analyzing response: {e}")
        return {
            "score": 0,
            "feedback": "Error analyzing response",
            "strengths": [],
            "improvements": []
        }

def parse_analysis_response(response: str) -> Dict[str, Any]:
    """Parse analysis response from LLM"""
    try:
        analysis = {
            "score": 0,
            "feedback": "",
            "strengths": [],
            "improvements": []
        }
        
        lines = response.split('\n')
        current_section = None
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            if line.startswith("SCORE:"):
                try:
                    score_str = line.replace("SCORE:", "").strip()
                    analysis["score"] = int(''.join(filter(str.isdigit, score_str)))
                except:
                    analysis["score"] = 0
            elif line.startswith("STRENGTHS:"):
                current_section = "strengths"
            elif line.startswith("IMPROVEMENTS:"):
                current_section = "improvements"
            elif line.startswith("FEEDBACK:"):
                current_section = "feedback"
                analysis["feedback"] = line.replace("FEEDBACK:", "").strip()
            elif line.startswith("- ") and current_section:
                point = line.replace("- ", "").strip()
                if current_section == "strengths":
                    analysis["strengths"].append(point)
                elif current_section == "improvements":
                    analysis["improvements"].append(point)
        
        return analysis
    except Exception as e:
        logger.error(f"Error parsing analysis: {e}")
        return {
            "score": 0,
            "feedback": "Error parsing analysis",
            "strengths": [],
            "improvements": []
        }
