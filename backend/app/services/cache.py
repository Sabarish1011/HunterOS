from redis.asyncio import Redis

from app.core.config import settings


class CacheService:
    def __init__(self, redis: Redis) -> None:
        self._redis = redis
        self._prefix = settings.redis_key_prefix

    def _key(self, key: str) -> str:
        return f"{self._prefix}:{key}"

    async def ping(self) -> bool:
        return await self._redis.ping()

    async def get(self, key: str) -> str | None:
        return await self._redis.get(self._key(key))

    async def set(self, key: str, value: str, ttl: int | None = None) -> None:
        await self._redis.set(self._key(key), value, ex=ttl)

    async def delete(self, key: str) -> None:
        await self._redis.delete(self._key(key))
