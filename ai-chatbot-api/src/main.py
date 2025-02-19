from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from src.api import endpoints, auth
from src.core.config import settings
from src.db.database import create_tables

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

@app.get("/health", tags=["health"])
async def health_check():
    """Health check endpoint"""
    return {"status": "ok"}

# Include routers
# app.include_router(auth.router, prefix="/api/v1", tags=["auth"])
app.include_router(endpoints.router, prefix="/api/v1", tags=["chatbot"])

@app.on_event("startup")
async def startup_event():
    create_tables()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)