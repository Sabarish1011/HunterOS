from uuid import UUID

from fastapi import APIRouter, Depends, status

from app.api.deps import get_opportunity_service
from app.schemas.opportunity import (
    OpportunityCreate,
    OpportunityResponse,
    OpportunityUpdate,
)
from app.services.opportunity import OpportunityService

router = APIRouter()


@router.get("", response_model=list[OpportunityResponse])
async def list_opportunities(
    service: OpportunityService = Depends(get_opportunity_service),
) -> list[OpportunityResponse]:
    return await service.list_opportunities()


@router.get("/{opportunity_id}", response_model=OpportunityResponse)
async def get_opportunity(
    opportunity_id: UUID,
    service: OpportunityService = Depends(get_opportunity_service),
) -> OpportunityResponse:
    return await service.get_opportunity(opportunity_id)


@router.post("", response_model=OpportunityResponse, status_code=status.HTTP_201_CREATED)
async def create_opportunity(
    data: OpportunityCreate,
    service: OpportunityService = Depends(get_opportunity_service),
) -> OpportunityResponse:
    return await service.create_opportunity(data)


@router.patch("/{opportunity_id}", response_model=OpportunityResponse)
async def update_opportunity(
    opportunity_id: UUID,
    data: OpportunityUpdate,
    service: OpportunityService = Depends(get_opportunity_service),
) -> OpportunityResponse:
    return await service.update_opportunity(opportunity_id, data)


@router.delete("/{opportunity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_opportunity(
    opportunity_id: UUID,
    service: OpportunityService = Depends(get_opportunity_service),
) -> None:
    await service.delete_opportunity(opportunity_id)
