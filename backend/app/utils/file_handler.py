import os
import logging
from pathlib import Path
from app.config import settings

logger = logging.getLogger(__name__)

def ensure_directories():
    """Ensure all required directories exist"""
    directories = [
        settings.UPLOAD_DIR,
        settings.GENERATED_DIR,
        settings.RECORDINGS_DIR
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        logger.info(f"Directory ensured: {directory}")

def save_uploaded_file(file_content: bytes, filename: str, directory: str = "uploads") -> str:
    """Save uploaded file to storage"""
    if directory == "uploads":
        save_path = os.path.join(settings.UPLOAD_DIR, filename)
    elif directory == "generated":
        save_path = os.path.join(settings.GENERATED_DIR, filename)
    elif directory == "recordings":
        save_path = os.path.join(settings.RECORDINGS_DIR, filename)
    else:
        save_path = os.path.join(settings.UPLOAD_DIR, filename)
    
    try:
        with open(save_path, 'wb') as f:
            f.write(file_content)
        logger.info(f"File saved: {save_path}")
        return save_path
    except Exception as e:
        logger.error(f"Error saving file: {e}")
        raise

def delete_file(file_path: str) -> bool:
    """Delete a file"""
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            logger.info(f"File deleted: {file_path}")
            return True
    except Exception as e:
        logger.error(f"Error deleting file: {e}")
    return False
