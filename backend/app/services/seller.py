from uuid import UUID

from app.core.exceptions import AppException
from app.repositories.seller import SellerRepository
from app.schemas.seller import (
    SellerCreate,
    SellerResponse,
    SellerUpdate,
)


class SellerService:
    def __init__(self, repository: SellerRepository) -> None:
        self._repository = repository

    async def list_sellers(self) -> list[SellerResponse]:
        sellers = await self._repository.list_all()
        return [SellerResponse.model_validate(s) for s in sellers]

    async def get_seller(self, seller_id: UUID) -> SellerResponse:
        seller = await self._repository.get_by_id(seller_id)

        if seller is None:
            raise AppException(
                "Seller not found",
                code="not_found",
                status_code=404,
            )

        return SellerResponse.model_validate(seller)

    async def create_seller(
        self,
        data: SellerCreate,
    ) -> SellerResponse:
        seller = await self._repository.create(data)
        return SellerResponse.model_validate(seller)

    async def update_seller(
        self,
        seller_id: UUID,
        data: SellerUpdate,
    ) -> SellerResponse:
        seller = await self._repository.get_by_id(seller_id)

        if seller is None:
            raise AppException(
                "Seller not found",
                code="not_found",
                status_code=404,
            )

        updated = await self._repository.update(seller, data)

        return SellerResponse.model_validate(updated)

    async def delete_seller(self, seller_id: UUID) -> None:
        seller = await self._repository.get_by_id(seller_id)

        if seller is None:
            raise AppException(
                "Seller not found",
                code="not_found",
                status_code=404,
            )

        await self._repository.delete(seller)
