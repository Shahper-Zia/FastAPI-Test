import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration settings for the application."""
    
    # FastAPI settings
    TITLE = os.getenv("API_TITLE", "AI-Powered Q&A Chatbot API")
    VERSION = os.getenv("API_VERSION", "1.0.0")
    
    # Database settings
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    
    # JWT settings
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
    ALGORITHM = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
    
    # Redis settings
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    
    # Logging settings
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")