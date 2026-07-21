from sqlalchemy.orm import Session

from app.models.message import Message


def get_all_messages(db: Session):
    """
    Return all customer messages ordered by newest first.
    """

    return (
        db.query(Message)
        .order_by(Message.created_at.desc())
        .all()
    )