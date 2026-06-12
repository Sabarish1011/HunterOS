-- HunterOS database initialization
-- Foundation schema only — no business logic

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- Schema version tracking for future migrations
CREATE TABLE IF NOT EXISTS schema_migrations (
    version     VARCHAR(255) PRIMARY KEY,
    applied_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

INSERT INTO schema_migrations (version)
VALUES ('001_init')
ON CONFLICT (version) DO NOTHING;
