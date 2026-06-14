from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class ListingBase(BaseModel):
    seller_id: UUID
    asset_id: UUID
    title: str = Field(..., min_length=1, max_length=255)
    asking_price: Decimal = Field(..., ge=0)
    source: str = Field(..., min_length=1, max_length=255)
    listing_url: str | None = Field(None, max_length=2048)
    status: str = Field(default="active", min_length=1, max_length=50)


class ListingCreate(ListingBase):
    pass


class ListingUpdate(BaseModel):
    seller_id: UUID | None = None
    asset_id: UUID | None = None
    title: str | None = Field(None, min_length=1, max_length=255)
    asking_price: Decimal | None = Field(None, ge=0)
    source: str | None = Field(None, min_length=1, max_length=255)
    listing_url: str | None = Field(None, max_length=2048)
    status: str | None = Field(None, min_length=1, max_length=50)


class ListingResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    seller_id: UUID
    asset_id: UUID
    title: str
    asking_price: Decimal
    source: str
    listing_url: str | None
    status: str
    opportunity_ids: list[UUID]
    created_at: datetime
