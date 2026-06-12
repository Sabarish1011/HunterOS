from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    app_name: str = "HunterOS"
    app_env: str = "development"
    app_debug: bool = True
    api_v1_prefix: str = "/api/v1"
    log_level: str = "INFO"

    host: str = "0.0.0.0"
    port: int = 8000

    postgres_host: str = "localhost"
    postgres_port: int = 5432
    postgres_user: str = "hunteros"
    postgres_password: str = "hunteros"
    postgres_db: str = "hunteros"
    db_pool_size: int = 5
    db_max_overflow: int = 10

    redis_host: str = "localhost"
    redis_port: int = 6379
    redis_db: int = 0
    redis_key_prefix: str = "hunteros"

    qdrant_host: str = "localhost"
    qdrant_port: int = 6333
    qdrant_grpc_port: int = 6334
    qdrant_collection_prefix: str = "hunteros_"
    qdrant_vector_size: int = 384

    cors_origins: str = "http://localhost:3000"

    @property
    def postgres_dsn(self) -> str:
        return (
            f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )

    @property
    def redis_url(self) -> str:
        return f"redis://{self.redis_host}:{self.redis_port}/{self.redis_db}"

    @property
    def cors_origins_list(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]


settings = Settings()
