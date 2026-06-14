from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.asset import Asset
from app.models.listing import Listing
from app.models.opportunity import Opportunity
from app.models.seller import Seller
from app.schemas.opportunity import OpportunityCreate, OpportunityUpdate


class OpportunityRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_by_id(self, opportunity_id: UUID) -> Opportunity | None:
        result = await self._session.execute(
            select(Opportunity)
            .options(
                selectinload(Opportunity.asset),
                selectinload(Opportunity.listing),
                selectinload(Opportunity.seller),
            )
            .where(Opportunity.id == opportunity_id)
        )
        return result.scalar_one_or_none()

    async def list_all(self) -> list[Opportunity]:
        result = await self._session.execute(
            select(Opportunity)
            .options(
                selectinload(Opportunity.asset),
                selectinload(Opportunity.listing),
                selectinload(Opportunity.seller),
            )
            .order_by(Opportunity.created_at.desc())
        )
        return list(result.scalars().all())

    async def asset_exists(self, asset_id: UUID) -> bool:
        return await self._session.get(Asset, asset_id) is not None

    async def listing_exists(self, listing_id: UUID) -> bool:
        return await self._session.get(Listing, listing_id) is not None

    async def seller_exists(self, seller_id: UUID) -> bool:
        return await self._session.get(Seller, seller_id) is not None

    async def create(self, data: OpportunityCreate) -> Opportunity:
        opportunity = Opportunity(**data.model_dump())
        self._session.add(opportunity)
        await self._session.commit()
        await self._session.refresh(opportunity)
        return opportunity

    async def update(
        self, opportunity: Opportunity, data: OpportunityUpdate
    ) -> Opportunity:
        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(opportunity, field, value)
        await self._session.commit()
        await self._session.refresh(opportunity)
        return opportunity

    async def delete(self, opportunity: Opportunity) -> None:
        await self._session.delete(opportunity)
        await self._session.commit()
