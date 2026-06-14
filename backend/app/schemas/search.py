from pydantic import BaseModel, ConfigDict

from app.schemas.asset import AssetResponse
from app.schemas.listing import ListingResponse
from app.schemas.opportunity import OpportunityResponse
from app.schemas.seller import SellerResponse


class SearchResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    assets: list[AssetResponse]
    listings: list[ListingResponse]
    sellers: list[SellerResponse]
    opportunities: list[OpportunityResponse]
