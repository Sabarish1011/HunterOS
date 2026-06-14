from uuid import UUID

from fastapi import APIRouter, Depends, status

from app.api.deps import get_asset_service
from app.schemas.asset import (
    AssetCreate,
    AssetResponse,
    AssetUpdate,
)
from app.services.asset import AssetService

router = APIRouter()


@router.get("", response_model=list[AssetResponse])
async def list_assets(
    service: AssetService = Depends(get_asset_service),
) -> list[AssetResponse]:
    return await service.list_assets()


@router.get("/{asset_id}", response_model=AssetResponse)
async def get_asset(
    asset_id: UUID,
    service: AssetService = Depends(get_asset_service),
) -> AssetResponse:
    return await service.get_asset(asset_id)


@router.post("", response_model=AssetResponse, status_code=status.HTTP_201_CREATED)
async def create_asset(
    data: AssetCreate,
    service: AssetService = Depends(get_asset_service),
) -> AssetResponse:
    return await service.create_asset(data)


@router.patch("/{asset_id}", response_model=AssetResponse)
async def update_asset(
    asset_id: UUID,
    data: AssetUpdate,
    service: AssetService = Depends(get_asset_service),
) -> AssetResponse:
    return await service.update_asset(asset_id, data)


@router.delete("/{asset_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_asset(
    asset_id: UUID,
    service: AssetService = Depends(get_asset_service),
) -> None:
    await service.delete_asset(asset_id)