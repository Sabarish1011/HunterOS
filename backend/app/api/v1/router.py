from fastapi import APIRouter

from app.api.v1.health import router as health_router
from app.api.v1.opportunities import router as opportunities_router

router = APIRouter()
router.include_router(health_router, tags=["health"])
router.include_router(opportunities_router, prefix="/opportunities", tags=["opportunities"])
