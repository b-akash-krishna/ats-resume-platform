import logging
from typing import Dict, List, Any
import re
from collections import Counter

logger = logging.getLogger(__name__)

# Common technical skills and keywords
TECHNICAL_SKILLS = {
    "programming": ["python", "java", "javascript", "typescript", "c++", "c#", "ruby", "php", "swift", "kotlin", "go", "rust", "scala"],
    "web_frameworks": ["react", "angular", "vue", "next.js", "nuxt", "svelte", "django", "flask", "fastapi", "express", "spring"],
    "databases": ["sql", "mysql", "postgresql", "mongodb", "redis", "elasticsearch", "cassandra", "dynamodb", "firestore"],
    "cloud": ["aws", "azure", "gcp", "heroku", "vercel", "netlify"],
    "devops": ["docker", "kubernetes", "jenkins", "gitlab", "github", "terraform", "ansible", "circleci"],
    "soft_skills": ["leadership", "communication", "teamwork", "problem-solving", "project management", "agile", "scrum"]
}

def calculate_ats_score(resume_text: str, job_description: str) -> Dict[str, Any]:
    """
    Calculate comprehensive ATS compatibility score between resume and job description
    """
    try:
        resume_lower = resume_text.lower()
        job_lower = job_description.lower()
        
        # Extract keywords
        resume_keywords = extract_keywords(resume_text)
        job_keywords = extract_keywords(job_description)
        
        # Compare keywords
        comparison = compare_keywords(resume_keywords, job_keywords)
        
        # Calculate base score from keyword matching
        keyword_score = comparison["match_percentage"]
        
        # Calculate skill score
        skill_score = calculate_skill_score(resume_lower, job_lower)
        
        # Calculate format score (check for common ATS-friendly elements)
        format_score = calculate_format_score(resume_text)
        
        # Weighted average: 50% keywords, 30% skills, 20% format
        final_score = (keyword_score * 0.5) + (skill_score * 0.3) + (format_score * 0.2)
        final_score = min(100, max(0, final_score))
        
        # Generate strengths and improvements
        strengths = generate_strengths(final_score, comparison, skill_score)
        improvements = generate_improvements(final_score, comparison, skill_score)
        
        logger.info(f"ATS score calculated: {final_score:.2f}")
        
        return {
            "score": round(final_score, 2),
            "keyword_score": round(keyword_score, 2),
            "skill_score": round(skill_score, 2),
            "format_score": round(format_score, 2),
            "strengths": strengths,
            "improvements": improvements,
            "matched_keywords": comparison["matched"][:10],
            "missing_keywords": comparison["missing"][:10]
        }
    except Exception as e:
        logger.error(f"Error calculating ATS score: {e}")
        return {
            "score": 0,
            "keyword_score": 0,
            "skill_score": 0,
            "format_score": 0,
            "strengths": [],
            "improvements": ["Error calculating score"],
            "matched_keywords": [],
            "missing_keywords": []
        }

def extract_keywords(text: str) -> List[str]:
    """
    Extract important keywords from text using stop word filtering
    """
    try:
        # Convert to lowercase and split
        words = text.lower().split()
        
        # Filter out common stop words
        stop_words = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
            'of', 'with', 'by', 'from', 'is', 'are', 'was', 'were', 'be', 'been',
            'have', 'has', 'do', 'does', 'did', 'will', 'would', 'could', 'should',
            'that', 'this', 'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they'
        }
        
        # Extract keywords (words longer than 3 chars, not stop words)
        keywords = [w.strip('.,;:!?') for w in words if w.strip('.,;:!?') not in stop_words and len(w.strip('.,;:!?')) > 3]
        
        logger.info(f"Extracted {len(keywords)} keywords")
        return keywords
    except Exception as e:
        logger.error(f"Error extracting keywords: {e}")
        return []

def compare_keywords(resume_keywords: List[str], job_keywords: List[str]) -> Dict[str, Any]:
    """
    Compare resume keywords with job description keywords
    """
    try:
        resume_set = set(resume_keywords)
        job_set = set(job_keywords)
        
        matched = resume_set.intersection(job_set)
        missing = job_set - resume_set
        
        match_percentage = (len(matched) / len(job_set) * 100) if job_set else 0
        
        logger.info(f"Keyword comparison: {len(matched)} matched, {len(missing)} missing")
        
        return {
            "matched": sorted(list(matched)),
            "missing": sorted(list(missing)),
            "match_percentage": match_percentage
        }
    except Exception as e:
        logger.error(f"Error comparing keywords: {e}")
        return {
            "matched": [],
            "missing": [],
            "match_percentage": 0.0
        }

def calculate_skill_score(resume_text: str, job_text: str) -> float:
    """
    Calculate skill match score based on technical skills
    """
    try:
        job_skills_found = 0
        total_job_skills = 0
        
        for category, skills in TECHNICAL_SKILLS.items():
            for skill in skills:
                if skill in job_text:
                    total_job_skills += 1
                    if skill in resume_text:
                        job_skills_found += 1
        
        skill_score = (job_skills_found / total_job_skills * 100) if total_job_skills > 0 else 0
        
        logger.info(f"Skill score: {skill_score:.2f}% ({job_skills_found}/{total_job_skills})")
        
        return skill_score
    except Exception as e:
        logger.error(f"Error calculating skill score: {e}")
        return 0.0

def calculate_format_score(resume_text: str) -> float:
    """
    Calculate ATS format compatibility score
    """
    try:
        score = 0
        max_score = 100
        
        # Check for common sections
        sections = ["experience", "education", "skills", "contact", "summary"]
        section_count = sum(1 for section in sections if section in resume_text.lower())
        score += (section_count / len(sections)) * 30
        
        # Check for contact information
        if re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', resume_text):
            score += 20
        
        if re.search(r'\b(?:\+?1[-.]?)?(?:\d{3})[-.]?(?:\d{3})[-.]?(?:\d{4})\b', resume_text):
            score += 20
        
        # Check for proper formatting (not too many special characters)
        special_char_ratio = len([c for c in resume_text if c in '!@#$%^&*()']) / len(resume_text)
        if special_char_ratio < 0.05:
            score += 15
        
        # Check for reasonable length
        word_count = len(resume_text.split())
        if 200 < word_count < 2000:
            score += 15
        
        logger.info(f"Format score: {score:.2f}")
        
        return min(score, max_score)
    except Exception as e:
        logger.error(f"Error calculating format score: {e}")
        return 0.0

def generate_strengths(score: float, comparison: Dict, skill_score: float) -> List[str]:
    """
    Generate strength feedback based on scores
    """
    strengths = []
    
    if score >= 80:
        strengths.append("Excellent ATS compatibility - strong keyword alignment")
    elif score >= 60:
        strengths.append("Good ATS compatibility - decent keyword coverage")
    
    if len(comparison["matched"]) > 5:
        strengths.append(f"Strong match on key terms: {', '.join(comparison['matched'][:3])}")
    
    if skill_score >= 70:
        strengths.append("Excellent technical skills alignment with job requirements")
    elif skill_score >= 50:
        strengths.append("Good technical skills coverage")
    
    if not strengths:
        strengths.append("Resume has basic ATS compatibility")
    
    return strengths

def generate_improvements(score: float, comparison: Dict, skill_score: float) -> List[str]:
    """
    Generate improvement suggestions based on scores
    """
    improvements = []
    
    if score < 70:
        improvements.append("Add more relevant keywords from the job description")
    
    if len(comparison["missing"]) > 0:
        top_missing = comparison["missing"][:5]
        improvements.append(f"Consider incorporating: {', '.join(top_missing)}")
    
    if skill_score < 60:
        improvements.append("Highlight more technical skills relevant to the position")
    
    if not improvements:
        improvements.append("Resume is well-optimized for ATS systems")
    
    return improvements
