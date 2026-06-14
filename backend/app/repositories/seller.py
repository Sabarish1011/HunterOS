from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.seller import Seller
from app.schemas.seller import SellerCreate, SellerUpdate


class SellerRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_by_id(self, seller_id: UUID) -> Seller | None:
        result = await self._session.execute(
            select(Seller)
            .options(
                selectinload(Seller.listings),
                selectinload(Seller.opportunities),
            )
            .where(Seller.id == seller_id)
        )
        return result.scalar_one_or_none()

    async def list_all(self) -> list[Seller]:
        result = await self._session.execute(
            select(Seller)
            .options(
                selectinload(Seller.listings),
                selectinload(Seller.opportunities),
            )
            .order_by(Seller.created_at.desc())
        )
        return list(result.scalars().all())

    async def create(self, data: SellerCreate) -> Seller:
        seller = Seller(**data.model_dump())
        self._session.add(seller)
        await self._session.commit()
        await self._session.refresh(seller)
        return seller

    async def update(
        self, seller: Seller, data: SellerUpdate
    ) -> Seller:
        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(seller, field, value)

        await self._session.commit()
        await self._session.refresh(seller)
        return seller

    async def delete(self, seller: Seller) -> None:
        await self._session.delete(seller)
        await self._session.commit()
