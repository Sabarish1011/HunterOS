from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class AssetBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    brand: str = Field(..., min_length=1, max_length=255)
    model: str = Field(..., min_length=1, max_length=255)
    category: str = Field(..., min_length=1, max_length=255)
    condition: str = Field(..., min_length=1, max_length=100)
    market_value: Decimal = Field(..., ge=0)


class AssetCreate(AssetBase):
    pass


class AssetUpdate(BaseModel):
    name: str | None = Field(None, min_length=1, max_length=255)
    brand: str | None = Field(None, min_length=1, max_length=255)
    model: str | None = Field(None, min_length=1, max_length=255)
    category: str | None = Field(None, min_length=1, max_length=255)
    condition: str | None = Field(None, min_length=1, max_length=100)
    market_value: Decimal | None = Field(None, ge=0)


class AssetResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    name: str
    brand: str
    model: str
    category: str
    condition: str
    market_value: Decimal
    listing_ids: list[UUID]
    opportunity_ids: list[UUID]
    created_at: datetime
