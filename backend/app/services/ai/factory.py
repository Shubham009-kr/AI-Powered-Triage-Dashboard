from app.core.config import get_settings
from app.services.ai.mock_provider import MockAIProvider
from app.services.ai.mistral_provider import MistralProvider


def get_ai_provider():
    settings = get_settings()

    if settings.AI_MODE == "mock":
        return MockAIProvider()

    return MistralProvider()
