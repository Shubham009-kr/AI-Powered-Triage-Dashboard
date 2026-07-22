from sqlalchemy.orm import Session
from app.models.message import Message
from datetime import datetime


def get_all_messages(db: Session):
    """
    Return all customer messages ordered by newest first.
    """

    return (
        db.query(Message)
        .order_by(Message.created_at.desc())
        .all()
    )

def get_message_by_id(db: Session, message_id: int):
    """
    Return a single message by its ID.  
    """
    return (
        db.query(Message)
        .filter(Message.id == message_id)
        .first()
    )

def mark_message_as_reviewed(db: Session, message_id: int):
    """
    Mark a message as reviewed.
    """

    message = (
        db.query(Message)
        .filter(Message.id == message_id)
        .first()
    )

    if message is None:
        return None

    if message.status != "reviewed":
        message.status = "reviewed"
        message.reviewed_at = datetime.utcnow()

    db.commit()
    db.refresh(message)

    return message