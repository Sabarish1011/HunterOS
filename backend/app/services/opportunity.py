from uuid import UUID

from app.core.exceptions import AppException
from app.repositories.opportunity import OpportunityRepository
from app.schemas.opportunity import (
    OpportunityCreate,
    OpportunityResponse,
    OpportunityUpdate,
)


class OpportunityService:
    def __init__(self, repository: OpportunityRepository) -> None:
        self._repository = repository

    async def list_opportunities(self) -> list[OpportunityResponse]:
        opportunities = await self._repository.list_all()
        return [OpportunityResponse.model_validate(o) for o in opportunities]

    async def get_opportunity(self, opportunity_id: UUID) -> OpportunityResponse:
        opportunity = await self._repository.get_by_id(opportunity_id)
        if opportunity is None:
            raise AppException("Opportunity not found", code="not_found", status_code=404)
        return OpportunityResponse.model_validate(opportunity)

    async def create_opportunity(self, data: OpportunityCreate) -> OpportunityResponse:
        opportunity = await self._repository.create(data)
        return OpportunityResponse.model_validate(opportunity)

    async def update_opportunity(
        self, opportunity_id: UUID, data: OpportunityUpdate
    ) -> OpportunityResponse:
        opportunity = await self._repository.get_by_id(opportunity_id)
        if opportunity is None:
            raise AppException("Opportunity not found", code="not_found", status_code=404)
        updated = await self._repository.update(opportunity, data)
        return OpportunityResponse.model_validate(updated)

    async def delete_opportunity(self, opportunity_id: UUID) -> None:
        opportunity = await self._repository.get_by_id(opportunity_id)
        if opportunity is None:
            raise AppException("Opportunity not found", code="not_found", status_code=404)
        await self._repository.delete(opportunity)
