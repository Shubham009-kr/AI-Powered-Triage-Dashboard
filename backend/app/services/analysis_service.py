from sqlalchemy.orm import Session

from app.models.analysis import Analysis
from app.models.message import Message
from app.services.ai.factory import get_ai_provider


async def analyze_message(db: Session, message_id: int):

    message = (
        db.query(Message)
        .filter(Message.id == message_id)
        .first()
    )

    if message is None:
        return None

    provider = get_ai_provider()

    result = await provider.analyze(message.text)

    analysis = (
        db.query(Analysis)
        .filter(Analysis.message_id == message.id)
        .first()
    )

    if analysis is None:
        analysis = Analysis(message_id=message.id)
        db.add(analysis)

    analysis.summary = result.summary
    analysis.category = result.category
    analysis.priority = result.priority
    analysis.confidence = result.confidence
    analysis.suggested_reply = result.suggested_reply

    db.commit()
    db.refresh(analysis)

    return analysis