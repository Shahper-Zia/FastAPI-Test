import redis
import json
from src.core.config import settings

redis_client = redis.from_url(settings.REDIS_URL)

class RedisCache:
    @staticmethod
    def get(key: str) -> str:
        value = redis_client.get(key)
        return value.decode('utf-8') if value else None

    @staticmethod
    def set(key: str, value: str, expire: int = 3600):
        redis_client.setex(key, expire, value)