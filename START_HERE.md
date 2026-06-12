# HunterOS — Foundation Build Guide

This file defines the foundation scaffold for HunterOS. Business logic is intentionally excluded.

## What Was Built

| Component      | Location          | Purpose                              |
|----------------|-------------------|--------------------------------------|
| Backend        | `backend/`        | FastAPI with health endpoints        |
| Frontend       | `frontend/`       | Next.js + Tailwind + Shadcn/UI       |
| Database       | `database/`       | PostgreSQL init scripts              |
| Infrastructure | `infrastructure/` | Docker Compose for all services    |
| Agents         | `agents/`         | Empty placeholder for LangGraph      |
| Docs           | `docs/`           | Architecture and dev guides          |

## Quick Start

```bash
make -C infrastructure up
```

## Next Steps

1. Define domain models and database schema
2. Add Alembic migrations
3. Implement API routes for arbitrage detection
4. Build frontend pages for monitoring and alerts
5. Add LangGraph agents in `agents/`

See `docs/` for full documentation.
