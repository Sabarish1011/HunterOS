from uuid import UUID

from app.core.exceptions import AppException
from app.repositories.listing import ListingRepository
from app.schemas.listing import (
    ListingCreate,
    ListingResponse,
    ListingUpdate,
)


class ListingService:
    def __init__(self, repository: ListingRepository) -> None:
        self._repository = repository

    async def _validate_related_ids(
        self,
        seller_id: UUID | None = None,
        asset_id: UUID | None = None,
    ) -> None:
        if seller_id is not None and not await self._repository.seller_exists(seller_id):
            raise AppException(
                "Seller not found",
                code="not_found",
                status_code=404,
            )

        if asset_id is not None and not await self._repository.asset_exists(asset_id):
            raise AppException(
                "Asset not found",
                code="not_found",
                status_code=404,
            )

    async def list_listings(self) -> list[ListingResponse]:
        listings = await self._repository.list_all()
        return [ListingResponse.model_validate(l) for l in listings]

    async def get_listing(self, listing_id: UUID) -> ListingResponse:
        listing = await self._repository.get_by_id(listing_id)

        if listing is None:
            raise AppException(
                "Listing not found",
                code="not_found",
                status_code=404,
            )

        return ListingResponse.model_validate(listing)

    async def create_listing(
        self,
        data: ListingCreate,
    ) -> ListingResponse:
        await self._validate_related_ids(
            seller_id=data.seller_id,
            asset_id=data.asset_id,
        )

        listing = await self._repository.create(data)
        return ListingResponse.model_validate(listing)

    async def update_listing(
        self,
        listing_id: UUID,
        data: ListingUpdate,
    ) -> ListingResponse:
        listing = await self._repository.get_by_id(listing_id)

        if listing is None:
            raise AppException(
                "Listing not found",
                code="not_found",
                status_code=404,
            )

        update_data = data.model_dump(exclude_unset=True)
        await self._validate_related_ids(
            seller_id=update_data.get("seller_id"),
            asset_id=update_data.get("asset_id"),
        )

        updated = await self._repository.update(listing, data)

        return ListingResponse.model_validate(updated)

    async def delete_listing(self, listing_id: UUID) -> None:
        listing = await self._repository.get_by_id(listing_id)

        if listing is None:
            raise AppException(
                "Listing not found",
                code="not_found",
                status_code=404,
            )

        await self._repository.delete(listing)
