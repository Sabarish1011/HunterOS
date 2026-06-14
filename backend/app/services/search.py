from sqlalchemy import or_, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.asset import Asset
from app.models.listing import Listing
from app.models.opportunity import Opportunity
from app.models.seller import Seller
from app.schemas.asset import AssetResponse
from app.schemas.listing import ListingResponse
from app.schemas.opportunity import OpportunityResponse
from app.schemas.search import SearchResponse
from app.schemas.seller import SellerResponse


class SearchService:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def _search_assets(self, term: str) -> list[AssetResponse]:
        result = await self._session.execute(
            select(Asset)
            .options(
                selectinload(Asset.listings),
                selectinload(Asset.opportunities),
            )
            .where(
                or_(
                    Asset.name.ilike(term),
                    Asset.brand.ilike(term),
                    Asset.model.ilike(term),
                    Asset.category.ilike(term),
                )
            )
            .order_by(Asset.created_at.desc())
            .limit(20)
        )
        return [AssetResponse.model_validate(asset) for asset in result.scalars().all()]

    async def _search_listings(self, term: str) -> list[ListingResponse]:
        result = await self._session.execute(
            select(Listing)
            .options(selectinload(Listing.opportunities))
            .where(
                or_(
                    Listing.title.ilike(term),
                    Listing.source.ilike(term),
                )
            )
            .order_by(Listing.created_at.desc())
            .limit(20)
        )
        return [ListingResponse.model_validate(listing) for listing in result.scalars().all()]

    async def _search_sellers(self, term: str) -> list[SellerResponse]:
        result = await self._session.execute(
            select(Seller)
            .options(
                selectinload(Seller.listings),
                selectinload(Seller.opportunities),
            )
            .where(
                or_(
                    Seller.name.ilike(term),
                    Seller.email.ilike(term),
                    Seller.location.ilike(term),
                )
            )
            .order_by(Seller.created_at.desc())
            .limit(20)
        )
        return [SellerResponse.model_validate(seller) for seller in result.scalars().all()]

    async def _search_opportunities(self, term: str) -> list[OpportunityResponse]:
        result = await self._session.execute(
            select(Opportunity)
            .where(Opportunity.title.ilike(term))
            .order_by(Opportunity.created_at.desc())
            .limit(20)
        )
        return [OpportunityResponse.model_validate(opportunity) for opportunity in result.scalars().all()]

    async def search(self, q: str) -> SearchResponse:
        term = q.strip()

        if not term:
            return SearchResponse(
                assets=[],
                listings=[],
                sellers=[],
                opportunities=[],
            )

        pattern = f"%{term}%"

        assets = await self._search_assets(pattern)
        listings = await self._search_listings(pattern)
        sellers = await self._search_sellers(pattern)
        opportunities = await self._search_opportunities(pattern)

        return SearchResponse(
            assets=assets,
            listings=listings,
            sellers=sellers,
            opportunities=opportunities,
        )
