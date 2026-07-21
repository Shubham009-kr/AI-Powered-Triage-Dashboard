from app.services.ai.base import (
    AIProvider,
    AIAnalysisResult,
)


class MistralProvider(AIProvider):

    async def analyze(self, message: str) -> AIAnalysisResult:
        raise NotImplementedError(
            "Mistral integration will be implemented next."
        )