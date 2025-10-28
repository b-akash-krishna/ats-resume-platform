import logging
from typing import Dict, Any
import re

logger = logging.getLogger(__name__)

def analyze_response(
    question: str,
    answer: str,
    category: str,
    difficulty: str = "medium"
) -> Dict[str, Any]:
    """
    Analyze interview response and provide score and feedback
    """
    try:
        # Calculate base score
        base_score = calculate_base_score(answer, category, difficulty)
        
        # Analyze response quality
        quality_metrics = analyze_response_quality(answer)
        
        # Adjust score based on quality
        final_score = base_score + quality_metrics["adjustment"]
        final_score = min(100, max(0, final_score))
        
        # Generate feedback
        feedback = generate_feedback(answer, category, quality_metrics, final_score)
        
        logger.info(f"Response analyzed: score={final_score:.2f}, category={category}")
        
        return {
            "score": round(final_score, 2),
            "base_score": round(base_score, 2),
            "quality_metrics": quality_metrics,
            "feedback": feedback,
            "category": category
        }
    except Exception as e:
        logger.error(f"Error analyzing response: {e}")
        return {
            "score": 50,
            "base_score": 50,
            "quality_metrics": {},
            "feedback": "Unable to analyze response",
            "category": category
        }

def calculate_base_score(answer: str, category: str, difficulty: str) -> float:
    """
    Calculate base score based on answer length and content
    """
    # Minimum word count for a good answer
    min_words = {"easy": 20, "medium": 40, "hard": 60}
    max_words = {"easy": 100, "medium": 200, "hard": 300}
    
    word_count = len(answer.split())
    min_w = min_words.get(difficulty, 40)
    max_w = max_words.get(difficulty, 200)
    
    # Score based on word count
    if word_count < min_w:
        score = (word_count / min_w) * 50
    elif word_count > max_w:
        score = 50 + ((max_w - word_count) / max_w) * 50
    else:
        score = 50 + ((word_count - min_w) / (max_w - min_w)) * 50
    
    return max(0, min(100, score))

def analyze_response_quality(answer: str) -> Dict[str, Any]:
    """
    Analyze various quality metrics of the response
    """
    metrics = {
        "has_examples": 0,
        "has_metrics": 0,
        "has_reflection": 0,
        "clarity_score": 0,
        "adjustment": 0
    }
    
    answer_lower = answer.lower()
    
    # Check for specific examples
    example_keywords = ["for example", "specifically", "instance", "case", "project", "situation"]
    if any(keyword in answer_lower for keyword in example_keywords):
        metrics["has_examples"] = 1
        metrics["adjustment"] += 10
    
    # Check for metrics/results
    metric_keywords = ["increased", "decreased", "improved", "reduced", "%", "number", "result"]
    if any(keyword in answer_lower for keyword in metric_keywords):
        metrics["has_metrics"] = 1
        metrics["adjustment"] += 10
    
    # Check for reflection/learning
    reflection_keywords = ["learned", "realized", "understood", "improved", "next time", "going forward"]
    if any(keyword in answer_lower for keyword in reflection_keywords):
        metrics["has_reflection"] = 1
        metrics["adjustment"] += 5
    
    # Calculate clarity score based on sentence structure
    sentences = answer.split('.')
    avg_sentence_length = len(answer.split()) / len(sentences) if sentences else 0
    
    if 10 < avg_sentence_length < 25:
        metrics["clarity_score"] = 1
        metrics["adjustment"] += 5
    
    # Cap adjustment
    metrics["adjustment"] = min(metrics["adjustment"], 30)
    
    return metrics

def generate_feedback(
    answer: str,
    category: str,
    quality_metrics: Dict,
    score: float
) -> str:
    """
    Generate constructive feedback for the response
    """
    feedback_parts = []
    
    if score >= 80:
        feedback_parts.append("Excellent response!")
    elif score >= 60:
        feedback_parts.append("Good response with room for improvement.")
    else:
        feedback_parts.append("Response needs more development.")
    
    # Specific feedback based on category
    if category == "behavioral":
        if not quality_metrics.get("has_examples"):
            feedback_parts.append("Consider including specific examples from your experience.")
        if not quality_metrics.get("has_reflection"):
            feedback_parts.append("Discuss what you learned from this experience.")
    
    elif category == "technical":
        if not quality_metrics.get("has_metrics"):
            feedback_parts.append("Include specific technical details or metrics in your answer.")
        if len(answer.split()) < 50:
            feedback_parts.append("Provide more detailed technical explanation.")
    
    elif category == "situational":
        if not quality_metrics.get("has_reflection"):
            feedback_parts.append("Explain your reasoning and how you would approach this situation.")
    
    # General feedback
    if not quality_metrics.get("clarity_score"):
        feedback_parts.append("Try to use clearer, more concise sentences.")
    
    return " ".join(feedback_parts)
