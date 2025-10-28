import logging
from typing import List, Tuple
import re

logger = logging.getLogger(__name__)

def validate_email(email: str) -> bool:
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_password(password: str) -> Tuple[bool, str]:
    """Validate password strength"""
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter"
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter"
    if not re.search(r'[0-9]', password):
        return False, "Password must contain at least one digit"
    return True, "Password is valid"

def validate_file_type(filename: str, allowed_types: List[str]) -> bool:
    """Validate file type"""
    file_extension = filename.split('.')[-1].lower()
    return file_extension in allowed_types

def validate_file_size(file_size: int, max_size_mb: int = 10) -> Tuple[bool, str]:
    """Validate file size"""
    max_bytes = max_size_mb * 1024 * 1024
    if file_size > max_bytes:
        return False, f"File size exceeds maximum of {max_size_mb}MB"
    return True, "File size is valid"

def validate_job_description(job_description: str) -> Tuple[bool, str]:
    """Validate job description"""
    if not job_description or len(job_description.strip()) == 0:
        return False, "Job description cannot be empty"
    if len(job_description) < 50:
        return False, "Job description must be at least 50 characters"
    if len(job_description) > 5000:
        return False, "Job description cannot exceed 5000 characters"
    return True, "Job description is valid"

def validate_interview_answer(answer: str) -> Tuple[bool, str]:
    """Validate interview answer"""
    if not answer or len(answer.strip()) == 0:
        return False, "Answer cannot be empty"
    if len(answer) < 10:
        return False, "Answer must be at least 10 characters"
    if len(answer) > 5000:
        return False, "Answer cannot exceed 5000 characters"
    return True, "Answer is valid"

def validate_difficulty_level(difficulty: str) -> Tuple[bool, str]:
    """Validate interview difficulty level"""
    valid_levels = ["easy", "medium", "hard"]
    if difficulty not in valid_levels:
        return False, f"Difficulty must be one of: {', '.join(valid_levels)}"
    return True, "Difficulty level is valid"
