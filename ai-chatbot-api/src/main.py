from fastapi import FastAPI
from api.endpoints import router as api_router
from core.config import settings
import uvicorn

app = FastAPI(title="AI-Powered Q&A Chatbot API")

# Include the API router
app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(app, host=settings.APP_HOST, port=settings.APP_PORT)