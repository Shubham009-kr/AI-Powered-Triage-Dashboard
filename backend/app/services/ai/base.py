from abc import ABC, abstractmethod

from app.schemas.ai import AIAnalysisResponse


class AIProvider(ABC):

    @abstractmethod
    async def analyze(
        self,
        message: str,
    ) -> AIAnalysisResponse:
        pass