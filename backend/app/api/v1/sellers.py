from uuid import UUID

from fastapi import APIRouter, Depends, status

from app.api.deps import get_seller_service
from app.schemas.seller import (
    SellerCreate,
    SellerResponse,
    SellerUpdate,
)
from app.services.seller import SellerService

router = APIRouter()


@router.get("", response_model=list[SellerResponse])
async def list_sellers(
    service: SellerService = Depends(get_seller_service),
) -> list[SellerResponse]:
    return await service.list_sellers()


@router.get("/{seller_id}", response_model=SellerResponse)
async def get_seller(
    seller_id: UUID,
    service: SellerService = Depends(get_seller_service),
) -> SellerResponse:
    return await service.get_seller(seller_id)


@router.post("", response_model=SellerResponse, status_code=status.HTTP_201_CREATED)
async def create_seller(
    data: SellerCreate,
    service: SellerService = Depends(get_seller_service),
) -> SellerResponse:
    return await service.create_seller(data)


@router.patch("/{seller_id}", response_model=SellerResponse)
async def update_seller(
    seller_id: UUID,
    data: SellerUpdate,
    service: SellerService = Depends(get_seller_service),
) -> SellerResponse:
    return await service.update_seller(seller_id, data)


@router.delete("/{seller_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_seller(
    seller_id: UUID,
    service: SellerService = Depends(get_seller_service),
) -> None:
    await service.delete_seller(seller_id)
