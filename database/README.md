# Database

PostgreSQL initialization and migration scaffolding for HunterOS.

## Structure

```
database/
├── init/           # Runs automatically on first Postgres container start
│   └── 001_init.sql
└── migrations/     # Future versioned migrations
    └── .gitkeep
```

## Initialization

When the Postgres container starts for the first time, scripts in `init/` are executed in alphabetical order. The initial script:

- Enables `uuid-ossp` and `pgcrypto` extensions
- Creates a `schema_migrations` table for tracking applied migrations

## Connection

| Setting  | Default   |
|----------|-----------|
| Host     | localhost |
| Port     | 5432      |
| User     | hunteros  |
| Password | hunteros  |
| Database | hunteros  |

## Future Migrations

Business tables will be added via versioned migration files in `migrations/`.
