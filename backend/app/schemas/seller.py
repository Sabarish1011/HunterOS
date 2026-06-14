from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class SellerBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    phone: str | None = Field(None, max_length=50)
    email: str | None = Field(None, max_length=255)
    location: str | None = Field(None, max_length=255)
    trust_score: Decimal = Field(default=Decimal("50"), ge=0, le=100)
    distress_score: Decimal = Field(default=Decimal("50"), ge=0, le=100)


class SellerCreate(SellerBase):
    pass


class SellerUpdate(BaseModel):
    name: str | None = Field(None, min_length=1, max_length=255)
    phone: str | None = Field(None, max_length=50)
    email: str | None = Field(None, max_length=255)
    location: str | None = Field(None, max_length=255)
    trust_score: Decimal | None = Field(None, ge=0, le=100)
    distress_score: Decimal | None = Field(None, ge=0, le=100)


class SellerResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    name: str
    phone: str | None
    email: str | None
    location: str | None
    trust_score: Decimal
    distress_score: Decimal
    listing_ids: list[UUID]
    opportunity_ids: list[UUID]
    created_at: datetime
