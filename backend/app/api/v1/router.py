from fastapi import APIRouter

from app.api.v1.assets import router as assets_router
from app.api.v1.health import router as health_router
from app.api.v1.listings import router as listings_router
from app.api.v1.opportunities import router as opportunities_router
from app.api.v1.search import router as search_router
from app.api.v1.sellers import router as sellers_router

router = APIRouter()

router.include_router(
    health_router,
    tags=["health"],
)

router.include_router(
    opportunities_router,
    prefix="/opportunities",
    tags=["opportunities"],
)

router.include_router(
    assets_router,
    prefix="/assets",
    tags=["assets"],
)

router.include_router(
    listings_router,
    prefix="/listings",
    tags=["listings"],
)

router.include_router(
    sellers_router,
    prefix="/sellers",
    tags=["sellers"],
)

router.include_router(
    search_router,
    prefix="/search",
    tags=["search"],
)
