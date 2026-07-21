from datetime import datetime
from pydantic import BaseModel, ConfigDict


class AnalysisResponse(BaseModel):
    id: int
    message_id: int
    summary: str
    category: str
    priority: str
    confidence: float
    suggested_reply: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)