import json
import re

from app.schemas.ai import AIAnalysisResponse
from app.core.exceptions import AIResponseParseError


def parse_ai_response(content: str) -> AIAnalysisResponse:
    """
    Extract and validate JSON returned by the LLM.
    """

    content = content.strip()

    # Remove markdown code fences if present
    content = re.sub(r"^```json\s*", "", content)
    content = re.sub(r"^```\s*", "", content)
    content = re.sub(r"\s*```$", "", content)

    # Extract JSON object
    start = content.find("{")
    end = content.rfind("}")

    if start == -1 or end == -1:
        raise AIResponseParseError("No JSON object found in AI response.")

    json_string = content[start : end + 1]

    try:
        data = json.loads(json_string)
        return AIAnalysisResponse.model_validate(data)
    except Exception as exc:
        raise AIResponseParseError(
            "Invalid AI response."
        ) from exc