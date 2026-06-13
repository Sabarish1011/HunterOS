from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.asset import Asset
from app.schemas.asset import AssetCreate, AssetUpdate


class AssetRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_by_id(self, asset_id: UUID) -> Asset | None:
        return await self._session.get(Asset, asset_id)

    async def list_all(self) -> list[Asset]:
        result = await self._session.execute(
            select(Asset).order_by(Asset.created_at.desc())
        )
        return list(result.scalars().all())

    async def create(self, data: AssetCreate) -> Asset:
        asset = Asset(**data.model_dump())
        self._session.add(asset)
        await self._session.commit()
        await self._session.refresh(asset)
        return asset

    async def update(
        self, asset: Asset, data: AssetUpdate
    ) -> Asset:
        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(asset, field, value)

        await self._session.commit()
        await self._session.refresh(asset)
        return asset

    async def delete(self, asset: Asset) -> None:
        await self._session.delete(asset)
        await self._session.commit()