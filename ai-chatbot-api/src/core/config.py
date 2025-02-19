from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    # FastAPI settings
    TITLE: str = "AI-Powered Q&A Chatbot API"
    VERSION: str = "1.0.0"
    
    # Database settings
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./database.db")
    
    # JWT settings
    JWT_SECRET: str = os.getenv("JWT_SECRET", "your_jwt_secret")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Redis settings
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379")
    
    # Gemini settings
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY")
    
    # Debug settings
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    
    class Config:
        case_sensitive = True

# Create settings instance
settings = Settings()