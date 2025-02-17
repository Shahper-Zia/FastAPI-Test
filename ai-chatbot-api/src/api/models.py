from pydantic import BaseModel
from typing import Optional

class UserQuery(BaseModel):
    question: str

class LLMResponse(BaseModel):
    answer: str
    confidence: Optional[float] = None

class ErrorResponse(BaseModel):
    detail: str