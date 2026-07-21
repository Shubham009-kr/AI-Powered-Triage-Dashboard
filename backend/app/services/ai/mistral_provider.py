from app.schemas.ai import AIAnalysisResponse
from app.services.ai.base import AIProvider
from app.prompts.analysis_prompt import build_analysis_prompt


class MistralProvider(AIProvider):

    async def analyze(
        self,
        message: str,
    ) -> AIAnalysisResponse:

        prompt = build_analysis_prompt(message)

        # We'll use this prompt when integrating the Mistral API.
        # For now, it's only prepared.

        raise NotImplementedError(
            "Mistral provider not implemented yet."
        )