import httpx

from app.core.config import get_settings

settings = get_settings()


def get_ai_client() -> httpx.AsyncClient:
    return httpx.AsyncClient(
        base_url="https://api.mistral.ai/v1",
        timeout=settings.AI_TIMEOUT,
        headers={
            "Authorization": f"Bearer {settings.MISTRAL_API_KEY}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )