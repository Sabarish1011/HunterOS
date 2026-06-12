# Development

Guide for running HunterOS services individually during development.

## Prerequisites

- Python 3.12+
- Node.js 22+
- Docker (for data services or full stack)

## Option 1: Full Docker Stack

See [Getting Started](./getting-started.md).

## Option 2: Hybrid (Recommended for Active Development)

Run data services in Docker, application code natively for hot reload.

### 1. Start Data Services

```bash
make -C infrastructure data-up
```

### 2. Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The default `.env.example` uses `localhost` for all data services. Docker Compose overrides these to container hostnames automatically.

### 3. Frontend

```bash
cd frontend
npm install
cp .env.example .env.local
npm run dev
```

Open http://localhost:3000.

## Project Layout

```
backend/
├── app/
│   ├── main.py
│   ├── core/           # config, lifespan, logging, exceptions
│   ├── db/             # SQLAlchemy base and session
│   ├── models/         # ORM models (future)
│   ├── schemas/        # Pydantic schemas
│   ├── services/       # cache, vector wrappers
│   └── api/
│       ├── deps.py     # Dependency injection
│       └── v1/         # Versioned routes
├── requirements.txt
└── Dockerfile

frontend/
├── app/                # Next.js App Router pages
├── components/
│   ├── ui/             # Shadcn/UI primitives
│   └── status/         # Status dashboard components
├── lib/
│   ├── api/            # Typed API client
│   └── utils.ts        # Shadcn cn() helper
├── types/              # TypeScript types
├── package.json
└── Dockerfile

agents/                 # Future LangGraph integration (empty)
```

## Adding New Backend Routes

1. Create a router in `backend/app/api/v1/`
2. Register it in `backend/app/api/v1/router.py`

## Database Migrations

Initial schema is in `database/init/001_init.sql`. Future changes go in `database/migrations/`.

## Linting

```bash
# Frontend
cd frontend && npm run lint
```

## Useful Commands

```bash
# View all container logs
make -C infrastructure logs

# Rebuild after Dockerfile changes
make -C infrastructure build

# Reset all data
make -C infrastructure clean && make -C infrastructure up
```

## Health Checks

| Endpoint | Purpose |
|----------|---------|
| `GET /api/v1/health` | Liveness — is the API process running? |
| `GET /api/v1/health/ready` | Readiness — can it reach postgres, redis, qdrant? |
