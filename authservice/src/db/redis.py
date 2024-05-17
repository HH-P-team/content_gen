from redis.asyncio import Redis
from db.base_storage import BaseAsyncCache
from core.settings import settings


class RedisRepository(BaseAsyncCache):
    """
    interface for Redis
    """

    redis = Redis(
        host=settings.redis_host,
        port=settings.redis_port,
        password=settings.redis_password,
    )

    async def get(self, key: str, **kwargs):
        """_getting data

        Args:
            key (str): key by element

        """

        data = await self.redis.get(key)
        return data

    async def set(
        self, key: str = None, value: str = None, expire: int = 600, **kwargs
    ) -> None:
        """push data to redis cash

        Args:
            key (str): key by element
        """
        if key and value:
            await self.redis.set(key, value, expire)
        if kwargs:
            for key, value in kwargs.items():
                await self.redis.set(key, value, expire)

    async def delete(self, key: str) -> None:
        """del data from redis by key name

        Args:
            key (str): key by element
        """

        await self.redis.delete(key)

    async def key_by_pattern(self, pattern):
        keys = await self.redis.keys(pattern)
        return keys
