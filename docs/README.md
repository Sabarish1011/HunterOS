# HunterOS Documentation

Technical documentation for the HunterOS platform foundation.

## Contents

| Document | Description |
|----------|-------------|
| [Getting Started](./getting-started.md) | Quick start guide |
| [Architecture](./architecture.md) | System design and component overview |
| [Development](./development.md) | Local development workflow |

## Project Structure

```
HunterOS/
├── backend/          FastAPI application
├── frontend/         Next.js application
├── database/         PostgreSQL init scripts and migrations
├── infrastructure/   Docker Compose and deployment config
└── docs/             Documentation
```

## Services

| Service    | Port  | Purpose                        |
|------------|-------|--------------------------------|
| Frontend   | 3000  | Web UI                         |
| Backend    | 8000  | REST API                       |
| PostgreSQL | 5432  | Primary relational database    |
| Redis      | 6379  | Caching and pub/sub            |
| Qdrant     | 6333  | Vector search                  |

## API Endpoints

| Method | Path                    | Description              |
|--------|-------------------------|--------------------------|
| GET    | `/`                     | API root                 |
| GET    | `/api/v1/health`        | Liveness check           |
| GET    | `/api/v1/health/ready`  | Readiness (infra checks) |
| GET    | `/docs`                 | Swagger UI               |
