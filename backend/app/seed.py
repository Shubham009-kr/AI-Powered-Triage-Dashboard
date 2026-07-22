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
        # Billing
        Message(
            customer_name="Priya Sharma",
            email="priya.sharma@example.com",
            text="I was charged twice for my monthly subscription. Please refund the extra amount.",
        ),
        Message(
            customer_name="Rahul Verma",
            email="rahul.verma@example.com",
            text="My credit card was charged, but my premium plan is still not activated.",
        ),

        # Login / Account
        Message(
            customer_name="Ananya Gupta",
            email="ananya.gupta@example.com",
            text="I reset my password yesterday, but I still can't log into my account.",
        ),
        Message(
            customer_name="Vikram Singh",
            email="vikram.singh@example.com",
            text="I'm getting an 'Invalid Credentials' error even though I'm entering the correct password.",
        ),

        # Complaint
        Message(
            customer_name="Neha Kapoor",
            email="neha.kapoor@example.com",
            text="I'm extremely disappointed with your service. Nobody has responded to my previous complaints.",
        ),
        Message(
            customer_name="Arjun Mehta",
            email="arjun.mehta@example.com",
            text="This is the third time I've contacted support, and my issue is still unresolved.",
        ),

        # Feature Request
        Message(
            customer_name="Sneha Iyer",
            email="sneha.iyer@example.com",
            text="It would be great if your app supported dark mode.",
        ),
        Message(
            customer_name="Rohan Nair",
            email="rohan.nair@example.com",
            text="Could you add an option to export reports as PDF files?",
        ),

        # Technical Bug
        Message(
            customer_name="Karan Patel",
            email="karan.patel@example.com",
            text="The dashboard crashes every time I try to upload a CSV file.",
        ),
        Message(
            customer_name="Aditi Joshi",
            email="aditi.joshi@example.com",
            text="The mobile app freezes on the payment screen after the latest update.",
        ),

        # Refund
        Message(
            customer_name="Manish Yadav",
            email="manish.yadav@example.com",
            text="I cancelled my subscription last week, but I haven't received my refund yet.",
        ),
        Message(
            customer_name="Pooja Mishra",
            email="pooja.mishra@example.com",
            text="I accidentally purchased the wrong plan. I'd like a refund, please.",
        ),

        # Security
        Message(
            customer_name="Suresh Reddy",
            email="suresh.reddy@example.com",
            text="I received a login alert from a device I don't recognize. Is my account compromised?",
        ),
        Message(
            customer_name="Kavya Menon",
            email="kavya.menon@example.com",
            text="Someone changed my account email without my permission. Please secure my account immediately.",
        ),

        # General Inquiry
        Message(
            customer_name="Aman Khanna",
            email="aman.khanna@example.com",
            text="Do you offer discounts for students or educational institutions?",
        ),
        Message(
            customer_name="Divya Rao",
            email="divya.rao@example.com",
            text="Can you explain the differences between your Basic and Premium plans?",
        ),
    ]

    db.add_all(sample_messages)
    db.commit()