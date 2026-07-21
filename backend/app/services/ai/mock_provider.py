from app.services.ai.base import (
    AIProvider,
    AIAnalysisResult,
)
from app.schemas.ai import AIAnalysisResponse


class MockAIProvider(AIProvider):

    async def analyze(self, message: str) -> AIAnalysisResult:

        return AIAnalysisResponse(
            summary="Customer payment issue.",
            category="Billing",
            priority="High",
            confidence=0.97,
            suggested_reply=(
                "We're sorry about the inconvenience. "
                "Our billing team is investigating your payment."
            ),
        )