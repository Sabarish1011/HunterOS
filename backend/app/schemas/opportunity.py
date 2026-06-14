from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field
from typing import Literal

from app.models.opportunity import OpportunityStatus


class OpportunityBase(BaseModel):
    asset_id: UUID | None = None
    listing_id: UUID | None = None
    seller_id: UUID | None = None
    title: str = Field(..., min_length=1, max_length=255)
    source: str = Field(..., min_length=1, max_length=255)
    asking_price: Decimal = Field(..., ge=0)
    estimated_value: Decimal = Field(..., ge=0)
    opportunity_score: Decimal = Field(..., ge=0, le=100)
    status: OpportunityStatus = OpportunityStatus.NEW


class OpportunityCreate(BaseModel):
    asset_id: UUID | None = None
    listing_id: UUID | None = None
    seller_id: UUID | None = None
    title: str = Field(..., min_length=1, max_length=255)
    source: str = Field(..., min_length=1, max_length=255)
    asking_price: Decimal = Field(..., ge=0)
    estimated_value: Decimal = Field(..., ge=0)
    opportunity_score: Decimal = Field(..., ge=0, le=100)
    status: OpportunityStatus = OpportunityStatus.NEW


class OpportunityUpdate(BaseModel):
    asset_id: UUID | None = None
    listing_id: UUID | None = None
    seller_id: UUID | None = None
    title: str | None = Field(None, min_length=1, max_length=255)
    source: str | None = Field(None, min_length=1, max_length=255)
    asking_price: Decimal | None = Field(None, ge=0)
    estimated_value: Decimal | None = Field(None, ge=0)
    opportunity_score: Decimal | None = Field(None, ge=0, le=100)
    status: OpportunityStatus | None = None


class OpportunityResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    asset_id: UUID | None
    listing_id: UUID | None
    seller_id: UUID | None
    title: str
    source: str
    asking_price: Decimal
    estimated_value: Decimal
    opportunity_score: Decimal
    status: OpportunityStatus
    created_at: datetime


class OpportunityAnalysisResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    value_gap: float
    profit_potential: float
    opportunity_score: float
    recommendation: Literal["IGNORE", "WATCH", "INVESTIGATE", "BUY"]
