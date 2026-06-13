from uuid import UUID

from app.core.exceptions import AppException
from app.repositories.asset import AssetRepository
from app.schemas.asset import (
    AssetCreate,
    AssetResponse,
    AssetUpdate,
)


class AssetService:
    def __init__(self, repository: AssetRepository) -> None:
        self._repository = repository

    async def list_assets(self) -> list[AssetResponse]:
        assets = await self._repository.list_all()
        return [AssetResponse.model_validate(a) for a in assets]

    async def get_asset(self, asset_id: UUID) -> AssetResponse:
        asset = await self._repository.get_by_id(asset_id)

        if asset is None:
            raise AppException(
                "Asset not found",
                code="not_found",
                status_code=404,
            )

        return AssetResponse.model_validate(asset)

    async def create_asset(
        self,
        data: AssetCreate,
    ) -> AssetResponse:
        asset = await self._repository.create(data)
        return AssetResponse.model_validate(asset)

    async def update_asset(
        self,
        asset_id: UUID,
        data: AssetUpdate,
    ) -> AssetResponse:
        asset = await self._repository.get_by_id(asset_id)

        if asset is None:
            raise AppException(
                "Asset not found",
                code="not_found",
                status_code=404,
            )

        updated = await self._repository.update(asset, data)

        return AssetResponse.model_validate(updated)

    async def delete_asset(self, asset_id: UUID) -> None:
        asset = await self._repository.get_by_id(asset_id)

        if asset is None:
            raise AppException(
                "Asset not found",
                code="not_found",
                status_code=404,
            )

        await self._repository.delete(asset)