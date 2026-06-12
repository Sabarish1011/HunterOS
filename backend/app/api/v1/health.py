from fastapi import APIRouter, Request
from sqlalchemy import text

from app.core.config import settings

router = APIRouter()


@router.get("/health")
async def health_check() -> dict:
    return {
        "status": "ok",
        "service": settings.app_name,
        "environment": settings.app_env,
    }


@router.get("/health/ready")
async def readiness_check(request: Request) -> dict:
    checks: dict[str, str] = {
        "postgres": "unknown",
        "redis": "unknown",
        "qdrant": "unknown",
    }

    try:
        async with request.app.state.db_engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
        checks["postgres"] = "ok"
    except Exception:
        checks["postgres"] = "error"

    try:
        await request.app.state.cache.ping()
        checks["redis"] = "ok"
    except Exception:
        checks["redis"] = "error"

    try:
        await request.app.state.vector.health_check()
        checks["qdrant"] = "ok"
    except Exception:
        checks["qdrant"] = "error"

    all_ok = all(status == "ok" for status in checks.values())

    return {
        "status": "ok" if all_ok else "degraded",
        "checks": checks,
    }
