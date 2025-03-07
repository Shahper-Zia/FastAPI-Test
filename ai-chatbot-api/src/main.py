from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from src.api.routers import auth, chat, health
from src.core.config import settings
from src.db.database import create_tables
from src.services.cache import RedisCache
from src.core.logger import logger

app = FastAPI(
    title="AI Chatbot API",
    description="AI-Powered Q&A Chatbot API using Gemini LLM",
    version="1.0.0"
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["root"])
async def root():
    """Redirect to API documentation"""
    return RedirectResponse(url="/docs")

# Include routers
app.include_router(health.router)
# app.include_router(auth.router, prefix="/api/v1")
app.include_router(chat.router)

@app.on_event("startup")
async def startup_event():
    logger.info("Hey there! I'm the AI Chatbot API. I'm ready to chat!")
    create_tables()

if __name__ == "__main__":
    import uvicorn

    # Initialize cache with error handling
    try:
        cache = RedisCache()
        CACHE_ENABLED = True
        logger.info("Redis cache initialized successfully...")
    except Exception as e:
        logger.warning(f"Redis cache initialization failed...: {e}")
        CACHE_ENABLED = False
    
    uvicorn.run(app, host="0.0.0.0", port=8000)