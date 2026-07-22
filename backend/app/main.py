from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI

from app.core.config import settings
from app.db.database import Base, SessionLocal, engine
from app.models import Analysis, Message
from app.seed import seed_messages
from app.api.routes.messages import router as message_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application startup and shutdown events.
    """

    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        seed_messages(db)
    finally:
        db.close()

    yield


app = FastAPI(
    title=settings.APP_NAME,
    description="AI-Powered Support Triage Dashboard",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(message_router)


@app.get("/", tags=["Health"])
async def health_check():
    """
        Health check endpoint to verify the application's status.
    """
    return {
        "status": "healthy",
        "application": settings.APP_NAME,
        "environment": settings.APP_ENV,
    }