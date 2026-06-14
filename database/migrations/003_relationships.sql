-- HunterOS: relationships between sellers, assets, listings, and opportunities

ALTER TABLE opportunities
    ADD COLUMN IF NOT EXISTS asset_id UUID,
    ADD COLUMN IF NOT EXISTS listing_id UUID,
    ADD COLUMN IF NOT EXISTS seller_id UUID;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint WHERE conname = 'listings_seller_id_fkey'
    ) THEN
        ALTER TABLE listings
            ADD CONSTRAINT listings_seller_id_fkey
            FOREIGN KEY (seller_id) REFERENCES sellers(id);
    END IF;

    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint WHERE conname = 'listings_asset_id_fkey'
    ) THEN
        ALTER TABLE listings
            ADD CONSTRAINT listings_asset_id_fkey
            FOREIGN KEY (asset_id) REFERENCES assets(id);
    END IF;

    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint WHERE conname = 'opportunities_asset_id_fkey'
    ) THEN
        ALTER TABLE opportunities
            ADD CONSTRAINT opportunities_asset_id_fkey
            FOREIGN KEY (asset_id) REFERENCES assets(id);
    END IF;

    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint WHERE conname = 'opportunities_listing_id_fkey'
    ) THEN
        ALTER TABLE opportunities
            ADD CONSTRAINT opportunities_listing_id_fkey
            FOREIGN KEY (listing_id) REFERENCES listings(id);
    END IF;

    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint WHERE conname = 'opportunities_seller_id_fkey'
    ) THEN
        ALTER TABLE opportunities
            ADD CONSTRAINT opportunities_seller_id_fkey
            FOREIGN KEY (seller_id) REFERENCES sellers(id);
    END IF;
END $$;

INSERT INTO schema_migrations (version)
VALUES ('003_relationships')
ON CONFLICT (version) DO NOTHING;
