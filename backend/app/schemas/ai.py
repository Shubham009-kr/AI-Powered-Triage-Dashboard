from pydantic import BaseModel, Field


class AIAnalysisResponse(BaseModel):
    summary: str
    category: str
    priority: str
    confidence: float = Field(ge=0.0, le=1.0)
    suggested_reply: str