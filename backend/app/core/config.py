from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""

    APP_NAME: str = "AI Support Triage Dashboard"
    APP_ENV: str = "development"
    DEBUG: bool = True

    DATABASE_URL: str = "sqlite:///./support_dashboard.db"

    AI_MODE: str = "mock"
    MISTRAL_API_KEY: str = ""
    MISTRAL_MODEL: str = "mistral-small-latest"
    AI_TIMEOUT: int = 30
    AI_MAX_RETRIES: int = 2

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """
    Returns a cached Settings object.

    The configuration is loaded only once during
    the application's lifetime.
    """
    return Settings()


settings = get_settings()