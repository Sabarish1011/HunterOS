from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.asset import Asset
from app.models.listing import Listing
from app.models.seller import Seller
from app.schemas.listing import ListingCreate, ListingUpdate


class ListingRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_by_id(self, listing_id: UUID) -> Listing | None:
        result = await self._session.execute(
            select(Listing)
            .options(selectinload(Listing.opportunities))
            .where(Listing.id == listing_id)
        )
        return result.scalar_one_or_none()

    async def list_all(self) -> list[Listing]:
        result = await self._session.execute(
            select(Listing)
            .options(selectinload(Listing.opportunities))
            .order_by(Listing.created_at.desc())
        )
        return list(result.scalars().all())

    async def seller_exists(self, seller_id: UUID) -> bool:
        return await self._session.get(Seller, seller_id) is not None

    async def asset_exists(self, asset_id: UUID) -> bool:
        return await self._session.get(Asset, asset_id) is not None

    async def create(self, data: ListingCreate) -> Listing:
        listing = Listing(**data.model_dump())
        self._session.add(listing)
        await self._session.commit()
        await self._session.refresh(listing)
        return listing

    async def update(
        self, listing: Listing, data: ListingUpdate
    ) -> Listing:
        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(listing, field, value)

        await self._session.commit()
        await self._session.refresh(listing)
        return listing

    async def delete(self, listing: Listing) -> None:
        await self._session.delete(listing)
        await self._session.commit()
