-- HunterOS: opportunities table

CREATE TABLE IF NOT EXISTS opportunities (
    id                UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    title             VARCHAR(255) NOT NULL,
    source            VARCHAR(255) NOT NULL,
    asking_price      NUMERIC(12, 2) NOT NULL,
    estimated_value   NUMERIC(12, 2) NOT NULL,
    opportunity_score NUMERIC(5, 2) NOT NULL,
    status            VARCHAR(20) NOT NULL DEFAULT 'new',
    created_at        TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

INSERT INTO schema_migrations (version)
VALUES ('002_opportunities')
ON CONFLICT (version) DO NOTHING;
