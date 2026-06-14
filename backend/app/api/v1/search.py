from fastapi import APIRouter, Depends, Query

from app.api.deps import get_search_service
from app.schemas.search import SearchResponse
from app.services.search import SearchService

router = APIRouter()


@router.get(
    "",
    response_model=SearchResponse,
    summary="Global search",
    description="Search across assets, listings, sellers, and opportunities using ilike matching.",
)
async def search(
    q: str = Query("", description="Search term"),
    service: SearchService = Depends(get_search_service),
) -> SearchResponse:
    return await service.search(q)
