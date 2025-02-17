from redis import Redis
from fastapi import HTTPException

class Cache:
    def __init__(self):
        self.redis = Redis(host='localhost', port=6379, db=0)

    def set(self, key: str, value: str, expire: int = 3600):
        try:
            self.redis.setex(key, expire, value)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Cache set error: {str(e)}")

    def get(self, key: str) -> str:
        try:
            value = self.redis.get(key)
            return value.decode('utf-8') if value else None
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Cache get error: {str(e)}")