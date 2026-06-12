# Getting Started

Run the full HunterOS stack locally with Docker Compose.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) 24+
- [Docker Compose](https://docs.docker.com/compose/) v2+

## Quick Start

1. Clone the repository:

```bash
git clone <repo-url>
cd HunterOS
```

2. Start all services:

```bash
make -C infrastructure up
```

Or directly:

```bash
docker compose -f infrastructure/docker-compose.yml up -d
```

3. Verify services are running:

```bash
make -C infrastructure ps
```

4. Open the applications:

| Service     | URL                          |
|-------------|------------------------------|
| Frontend    | http://localhost:3000        |
| Backend API | http://localhost:8000        |
| API Docs    | http://localhost:8000/docs   |
| Qdrant UI   | http://localhost:6333/dashboard |

5. Check health:

```bash
curl http://localhost:8000/api/v1/health
curl http://localhost:8000/api/v1/health/ready
```

## Stop Services

```bash
make -C infrastructure down
```

To remove volumes as well:

```bash
make -C infrastructure clean
```

## Environment Variables

Copy example env files and customize if needed:

```bash
cp infrastructure/.env.example infrastructure/.env
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env.local
```

Defaults work out of the box for local development.

## Next Steps

See [Development](./development.md) for running services individually without Docker.
