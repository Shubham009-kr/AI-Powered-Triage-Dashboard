import httpx

from app.core.config import get_settings
from app.prompts.analysis_prompt import build_analysis_prompt
from app.schemas.ai import AIAnalysisResponse
from app.services.ai.base import AIProvider
from app.services.ai.parser import parse_ai_response
from app.services.ai.client import get_ai_client
from app.core.exceptions import AIProviderError

settings = get_settings()


class MistralProvider(AIProvider):

    async def analyze(
        self,
        message: str,
    ) -> AIAnalysisResponse:

        prompt = build_analysis_prompt(message)

        payload = {
            "model": settings.MISTRAL_MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            "temperature": 0.2,
        }

        try:
            async with get_ai_client() as client:

                response = await client.post(
                    "/chat/completions",
                    json=payload,
                )

                response.raise_for_status()

                data = response.json()
            content = data["choices"][0]["message"]["content"]
            return parse_ai_response(content)
        except httpx.HTTPStatusError as exc:
            raise AIProviderError(
                f"Mistral API returned {exc.response.status_code}"
            ) from exc

        except httpx.RequestError as exc:
            raise AIProviderError(
                "Unable to connect to the Mistral API."
            ) from exc
