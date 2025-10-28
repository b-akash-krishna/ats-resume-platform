import logging
import httpx
from app.config import settings

logger = logging.getLogger(__name__)

async def generate_text(prompt: str, model: str = None) -> str:
    """
    Generate text using Ollama LLM
    
    TODO: Implement Ollama integration for text generation
    """
    if model is None:
        model = settings.OLLAMA_MODEL
    
    logger.info(f"Generating text with model: {model}")
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{settings.OLLAMA_BASE_URL}/api/generate",
                json={
                    "model": model,
                    "prompt": prompt,
                    "stream": False
                }
            )
            if response.status_code == 200:
                return response.json().get("response", "")
    except Exception as e:
        logger.error(f"Error generating text: {e}")
    
    return ""

async def generate_embeddings(text: str) -> List[float]:
    """
    Generate embeddings for text using sentence-transformers
    
    TODO: Implement embedding generation
    """
    logger.info("Generating embeddings")
    return []
