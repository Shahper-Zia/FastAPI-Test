from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.api.models import QueryRequest, QueryResponse
from src.services.llm import get_llm_response
from src.services.cache import RedisCache
from src.db.database import get_db, Query
from src.core.logger import logger
import hashlib

router = APIRouter(
    prefix="/api/v1",
    tags=["chatbot"]
    )

# Initialize cache with error handling
try:
    cache = RedisCache()
    CACHE_ENABLED = True
    logger.info("Redis cache initialized successfully-lol")
except Exception as e:
    logger.warning(f"Redis cache initialization failed-lol: {e}")
    CACHE_ENABLED = False

@router.post("/query")
async def create_query(
    query: QueryRequest,
    db: Session = Depends(get_db)
):
    response = None
    is_cached = False
    cache_key = None

    if CACHE_ENABLED:
        try:
            # Generate cache key
            cache_key = hashlib.md5(query.question.encode()).hexdigest()
            logger.info(f"Checking cache for key: {cache_key}")
            
            # Check cache
            cached_response = cache.get(cache_key)
            if cached_response:
                logger.info(f"Cache hit for question: {query.question[:50]}...")
                return QueryResponse(
                    response=cached_response, 
                    cached=True,
                    message="Response retrieved from cache"
                )
            logger.info("Cache miss - fetching from LLM")
        except Exception as e:
            logger.error(f"Cache error: {e}")
            # Continue without cache if there's an error
    
    # Get response from LLM
    response = await get_llm_response(query.question)
    
    # Try to cache the response if caching is enabled
    if CACHE_ENABLED:
        try:
            cache.set(cache_key, response)
            logger.info(f"Cached response for key: {cache_key}")
        except Exception as e:
            logger.error(f"Cache storage error: {e}")
    
    # Log to database
    db_query = Query(
        user_id="anonymous",
        question=query.question,
        response=response
    )
    db.add(db_query)
    db.commit()
    
    return QueryResponse(
        response=response, 
        cached=False,
        message="Response generated from LLM"
    )