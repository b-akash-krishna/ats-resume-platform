import logging
from typing import List, Dict
import random

logger = logging.getLogger(__name__)

# Pre-defined question templates for different categories and difficulties
QUESTION_TEMPLATES = {
    "behavioral": {
        "easy": [
            "Tell me about yourself and your professional background.",
            "Why are you interested in this position?",
            "What are your greatest strengths?",
            "Describe a time when you had to learn something new quickly.",
            "How do you handle feedback from colleagues?"
        ],
        "medium": [
            "Tell me about a time you had to work with a difficult team member. How did you handle it?",
            "Describe a situation where you had to meet a tight deadline. What was your approach?",
            "Give an example of when you took initiative on a project.",
            "Tell me about a time you failed. What did you learn from it?",
            "Describe a situation where you had to adapt to change."
        ],
        "hard": [
            "Tell me about a time you had to make a difficult decision with incomplete information.",
            "Describe a situation where you had to lead a team through a major challenge.",
            "Give an example of when you had to influence someone without direct authority.",
            "Tell me about a time you had to balance competing priorities.",
            "Describe a situation where you had to take responsibility for a team's failure."
        ]
    },
    "technical": {
        "easy": [
            "What programming languages are you proficient in?",
            "Explain the difference between a list and a dictionary.",
            "What is version control and why is it important?",
            "Describe the basic structure of a web application.",
            "What is the difference between SQL and NoSQL databases?"
        ],
        "medium": [
            "How would you optimize a slow database query?",
            "Explain the concept of RESTful APIs and their benefits.",
            "What is the difference between synchronous and asynchronous programming?",
            "How would you approach debugging a complex issue in production?",
            "Explain the MVC architecture pattern."
        ],
        "hard": [
            "Design a system to handle millions of concurrent users.",
            "How would you implement caching in a distributed system?",
            "Explain the CAP theorem and its implications.",
            "How would you approach optimizing a microservices architecture?",
            "Design a real-time notification system for a social media platform."
        ]
    },
    "situational": {
        "easy": [
            "What would you do if you didn't understand a task assigned to you?",
            "If you had to choose between speed and quality, how would you decide?",
            "What would you do if you discovered a bug in production?",
            "How would you handle a situation where you disagree with your manager?",
            "What would you do if a project deadline was moved up?"
        ],
        "medium": [
            "If you had to choose between helping a colleague or meeting your own deadline, what would you do?",
            "What would you do if you realized you made a mistake that affected the team?",
            "How would you handle a situation where you had to work with someone you didn't get along with?",
            "If a client requested a feature that goes against best practices, how would you handle it?",
            "What would you do if you felt overwhelmed by your workload?"
        ],
        "hard": [
            "If you had to choose between being right and maintaining team harmony, what would you do?",
            "How would you handle a situation where your team was resistant to necessary changes?",
            "If you discovered a colleague was underperforming, how would you address it?",
            "What would you do if you had to deliver bad news to stakeholders?",
            "If you had to make a decision that would disappoint some team members, how would you approach it?"
        ]
    }
}

def generate_interview_questions(
    job_description: str,
    job_title: str,
    difficulty: str = "medium",
    count: int = 5
) -> List[Dict[str, str]]:
    """
    Generate interview questions based on job description and difficulty level
    """
    try:
        questions = []
        
        # Determine which categories to use based on job description
        categories = determine_question_categories(job_description)
        
        # Generate questions from templates
        for category in categories:
            if category in QUESTION_TEMPLATES:
                template_questions = QUESTION_TEMPLATES[category].get(difficulty, QUESTION_TEMPLATES[category]["medium"])
                selected = random.sample(template_questions, min(len(template_questions), count // len(categories) + 1))
                
                for q in selected:
                    questions.append({
                        "question": q,
                        "category": category
                    })
        
        # Ensure we have the requested count
        if len(questions) < count:
            remaining = count - len(questions)
            all_questions = [q for cat_q in QUESTION_TEMPLATES.values() for q in cat_q.get(difficulty, [])]
            additional = random.sample(all_questions, min(len(all_questions), remaining))
            questions.extend([{"question": q, "category": "general"} for q in additional])
        
        questions = questions[:count]
        
        logger.info(f"Generated {len(questions)} interview questions for {job_title}")
        return questions
    except Exception as e:
        logger.error(f"Error generating questions: {e}")
        return get_default_questions(count)

def determine_question_categories(job_description: str) -> List[str]:
    """
    Determine which question categories to use based on job description
    """
    categories = ["behavioral"]  # Always include behavioral
    
    job_lower = job_description.lower()
    
    # Check for technical keywords
    technical_keywords = ["python", "java", "javascript", "sql", "api", "database", "code", "algorithm", "system design"]
    if any(keyword in job_lower for keyword in technical_keywords):
        categories.append("technical")
    
    # Check for situational keywords
    situational_keywords = ["leadership", "manage", "team", "project", "decision", "problem-solving"]
    if any(keyword in job_lower for keyword in situational_keywords):
        categories.append("situational")
    
    return categories

def get_default_questions(count: int) -> List[Dict[str, str]]:
    """
    Get default questions if generation fails
    """
    default_questions = [
        {"question": "Tell me about yourself.", "category": "behavioral"},
        {"question": "Why are you interested in this position?", "category": "behavioral"},
        {"question": "What are your greatest strengths?", "category": "behavioral"},
        {"question": "Describe a challenge you overcame.", "category": "behavioral"},
        {"question": "Where do you see yourself in 5 years?", "category": "behavioral"}
    ]
    
    return default_questions[:count]

def categorize_question(question: str) -> str:
    """
    Categorize interview question based on keywords
    """
    question_lower = question.lower()
    
    behavioral_keywords = ["tell me about", "describe", "experience", "challenge", "conflict", "yourself", "strengths", "weakness"]
    technical_keywords = ["how", "implement", "design", "algorithm", "code", "technical", "system", "database", "api"]
    situational_keywords = ["what would you", "if you", "scenario", "situation", "would you"]
    
    for keyword in behavioral_keywords:
        if keyword in question_lower:
            return "behavioral"
    
    for keyword in technical_keywords:
        if keyword in question_lower:
            return "technical"
    
    for keyword in situational_keywords:
        if keyword in question_lower:
            return "situational"
    
    return "general"
