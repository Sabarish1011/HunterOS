# Infrastructure

Docker Compose orchestration for HunterOS.

## Quick Start

```bash
make up
```

## Data Services Only (Hybrid Dev)

```bash
make data-up
```

Runs postgres, redis, and qdrant. Start backend and frontend natively for hot reload.

## Commands

| Command       | Description              |
|---------------|--------------------------|
| `make up`     | Start all services       |
| `make down`   | Stop all services        |
| `make build`  | Rebuild images           |
| `make logs`   | Tail container logs      |
| `make ps`     | Show service status      |
| `make clean`  | Stop and remove volumes  |
| `make data-up`| Start data services only |
