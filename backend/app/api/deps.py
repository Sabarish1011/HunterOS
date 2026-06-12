from collections.abc import AsyncIterator

from fastapi import Depends, Request
from qdrant_client import AsyncQdrantClient
from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.opportunity import OpportunityRepository
from app.services.cache import CacheService
from app.services.opportunity import OpportunityService
from app.services.vector import VectorService


async def get_db(request: Request) -> AsyncIterator[AsyncSession]:
    session_factory = request.app.state.db_session_factory
    async with session_factory() as session:
        yield session


def get_redis(request: Request) -> Redis:
    return request.app.state.redis


def get_cache(request: Request) -> CacheService:
    return request.app.state.cache


def get_qdrant(request: Request) -> AsyncQdrantClient:
    return request.app.state.qdrant


def get_vector(request: Request) -> VectorService:
    return request.app.state.vector


async def get_opportunity_service(
    session: AsyncSession = Depends(get_db),
) -> OpportunityService:
    return OpportunityService(OpportunityRepository(session))
