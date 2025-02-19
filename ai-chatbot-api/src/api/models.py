from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Token(BaseModel):
    access_token: str
    token_type: str

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    response: str
    cached: bool
    message: str = "Response processed successfully"

class QueryLog(BaseModel):
    id: int
    user_id: str
    question: str
    response: str
    timestamp: datetime

    class Config:
        from_attributes = True