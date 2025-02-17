from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.llm import get_llm_response
from services.cache import cache_response

router = APIRouter()

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    answer: str

@router.post("/query", response_model=QueryResponse)
async def handle_query(request: QueryRequest):
    try:
        # Check if the response is cached
        cached_answer = await cache_response(request.question)
        if cached_answer:
            return QueryResponse(answer=cached_answer)

        # Get response from the LLM
        answer = await get_llm_response(request.question)

        # Cache the response
        await cache_response(request.question, answer)

        return QueryResponse(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))