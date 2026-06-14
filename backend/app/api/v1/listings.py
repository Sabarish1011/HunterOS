from uuid import UUID

from fastapi import APIRouter, Depends, status

from app.api.deps import get_listing_service
from app.schemas.listing import (
    ListingCreate,
    ListingResponse,
    ListingUpdate,
)
from app.services.listing import ListingService

router = APIRouter()


@router.get("", response_model=list[ListingResponse])
async def list_listings(
    service: ListingService = Depends(get_listing_service),
) -> list[ListingResponse]:
    return await service.list_listings()


@router.get("/{listing_id}", response_model=ListingResponse)
async def get_listing(
    listing_id: UUID,
    service: ListingService = Depends(get_listing_service),
) -> ListingResponse:
    return await service.get_listing(listing_id)


@router.post("", response_model=ListingResponse, status_code=status.HTTP_201_CREATED)
async def create_listing(
    data: ListingCreate,
    service: ListingService = Depends(get_listing_service),
) -> ListingResponse:
    return await service.create_listing(data)


@router.patch("/{listing_id}", response_model=ListingResponse)
async def update_listing(
    listing_id: UUID,
    data: ListingUpdate,
    service: ListingService = Depends(get_listing_service),
) -> ListingResponse:
    return await service.update_listing(listing_id, data)


@router.delete("/{listing_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_listing(
    listing_id: UUID,
    service: ListingService = Depends(get_listing_service),
) -> None:
    await service.delete_listing(listing_id)
