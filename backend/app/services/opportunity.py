from uuid import UUID

from app.core.exceptions import AppException
from app.repositories.opportunity import OpportunityRepository
from app.schemas.opportunity import (
    OpportunityCreate,
    OpportunityAnalysisResponse,
    OpportunityResponse,
    OpportunityUpdate,
)
from app.services.opportunity_engine import OpportunityAnalysisEngine


class OpportunityService:
    def __init__(self, repository: OpportunityRepository) -> None:
        self._repository = repository
        self._engine = OpportunityAnalysisEngine()

    async def _validate_related_ids(
        self,
        asset_id: UUID | None = None,
        listing_id: UUID | None = None,
        seller_id: UUID | None = None,
    ) -> None:
        if asset_id is not None and not await self._repository.asset_exists(asset_id):
            raise AppException("Asset not found", code="not_found", status_code=404)

        if listing_id is not None and not await self._repository.listing_exists(listing_id):
            raise AppException("Listing not found", code="not_found", status_code=404)

        if seller_id is not None and not await self._repository.seller_exists(seller_id):
            raise AppException("Seller not found", code="not_found", status_code=404)

    async def list_opportunities(self) -> list[OpportunityResponse]:
        opportunities = await self._repository.list_all()
        return [OpportunityResponse.model_validate(o) for o in opportunities]

    async def get_opportunity(self, opportunity_id: UUID) -> OpportunityResponse:
        opportunity = await self._repository.get_by_id(opportunity_id)
        if opportunity is None:
            raise AppException("Opportunity not found", code="not_found", status_code=404)
        return OpportunityResponse.model_validate(opportunity)

    async def create_opportunity(self, data: OpportunityCreate) -> OpportunityResponse:
        await self._validate_related_ids(
            asset_id=data.asset_id,
            listing_id=data.listing_id,
            seller_id=data.seller_id,
        )

        opportunity = await self._repository.create(data)
        return OpportunityResponse.model_validate(opportunity)

    async def update_opportunity(
        self, opportunity_id: UUID, data: OpportunityUpdate
    ) -> OpportunityResponse:
        opportunity = await self._repository.get_by_id(opportunity_id)
        if opportunity is None:
            raise AppException("Opportunity not found", code="not_found", status_code=404)

        update_data = data.model_dump(exclude_unset=True)
        await self._validate_related_ids(
            asset_id=update_data.get("asset_id"),
            listing_id=update_data.get("listing_id"),
            seller_id=update_data.get("seller_id"),
        )

        updated = await self._repository.update(opportunity, data)
        return OpportunityResponse.model_validate(updated)

    async def delete_opportunity(self, opportunity_id: UUID) -> None:
        opportunity = await self._repository.get_by_id(opportunity_id)
        if opportunity is None:
            raise AppException("Opportunity not found", code="not_found", status_code=404)
        await self._repository.delete(opportunity)

    async def analyze_opportunity(
        self,
        opportunity_id: UUID,
    ) -> OpportunityAnalysisResponse:
        opportunity = await self._repository.get_by_id(opportunity_id)

        if opportunity is None:
            raise AppException("Opportunity not found", code="not_found", status_code=404)

        if opportunity.listing is None or opportunity.asset is None or opportunity.seller is None:
            raise AppException(
                "Opportunity is missing related listing, asset, or seller",
                code="invalid_state",
                status_code=422,
            )

        analysis = self._engine.analyze(
            opportunity.listing,
            opportunity.asset,
            opportunity.seller,
        )

        return OpportunityAnalysisResponse.model_validate(analysis)
