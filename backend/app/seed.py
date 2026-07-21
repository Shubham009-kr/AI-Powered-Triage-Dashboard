from sqlalchemy.orm import Session

from app.models.message import Message


def seed_messages(db: Session) -> None:
    """
    Seed initial sample messages if the database is empty.
    """

    existing = db.query(Message).first()

    if existing:
        return

    sample_messages = [
        Message(
            customer_name="John Doe",
            email="john@example.com",
            text="I was charged twice for my subscription.",
        ),
        Message(
            customer_name="Alice Smith",
            email="alice@example.com",
            text="I cannot log into my account after resetting my password.",
        ),
    ]

    db.add_all(sample_messages)
    db.commit()