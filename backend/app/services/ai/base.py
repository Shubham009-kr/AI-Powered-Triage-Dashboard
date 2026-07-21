from abc import ABC, abstractmethod
from typing import TypedDict


class AIAnalysisResult(TypedDict):
    summary: str
    category: str
    priority: str
    confidence: float
    suggested_reply: str


class AIProvider(ABC):

    @abstractmethod
    async def analyze(self, message: str) -> AIAnalysisResult:
        pass