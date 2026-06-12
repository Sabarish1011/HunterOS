# HunterOS

Price arbitrage monitoring platform.

## Stack

| Layer          | Technology              |
|----------------|-------------------------|
| Frontend       | Next.js 15, Tailwind CSS, Shadcn/UI |
| Backend        | FastAPI                 |
| Database       | PostgreSQL 16           |
| Cache          | Redis 7                 |
| Vector Store   | Qdrant 1.12             |
| Infrastructure | Docker Compose          |
| Agents         | LangGraph (future)      |

## Quick Start

```bash
make -C infrastructure up
```

| Service  | URL                        |
|----------|----------------------------|
| Frontend | http://localhost:3000      |
| API      | http://localhost:8000      |
| API Docs | http://localhost:8000/docs   |

## Project Structure

```
HunterOS/
├── backend/          FastAPI application
├── frontend/         Next.js application
├── database/         PostgreSQL init scripts
├── infrastructure/   Docker Compose orchestration
├── agents/           Future LangGraph agents (empty)
└── docs/             Documentation
```

## Documentation

- [Getting Started](./docs/getting-started.md)
- [Architecture](./docs/architecture.md)
- [Development](./docs/development.md)

## Status

Foundation scaffold — health checks and service wiring only. Business logic not yet implemented.
