from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.opportunity import Opportunity
from app.schemas.opportunity import OpportunityCreate, OpportunityUpdate


class OpportunityRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_by_id(self, opportunity_id: UUID) -> Opportunity | None:
        return await self._session.get(Opportunity, opportunity_id)

    async def list_all(self) -> list[Opportunity]:
        result = await self._session.execute(
            select(Opportunity).order_by(Opportunity.created_at.desc())
        )
        return list(result.scalars().all())

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
