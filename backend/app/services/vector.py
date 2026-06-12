from qdrant_client import AsyncQdrantClient
from qdrant_client.models import Distance, VectorParams

from app.core.config import settings


class VectorService:
    def __init__(self, client: AsyncQdrantClient) -> None:
        self._client = client

    @property
    def system_collection(self) -> str:
        return f"{settings.qdrant_collection_prefix}system"

    async def health_check(self) -> bool:
        await self._client.get_collections()
        return True

    async def ensure_system_collection(self) -> None:
        collections = await self._client.get_collections()
        names = {c.name for c in collections.collections}
        if self.system_collection not in names:
            await self._client.create_collection(
                collection_name=self.system_collection,
                vectors_config=VectorParams(
                    size=settings.qdrant_vector_size,
                    distance=Distance.COSINE,
                ),
            )
