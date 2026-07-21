from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.message import MessageResponse
from app.services.message_service import get_all_messages

router = APIRouter(prefix="/messages", tags=["Messages"])


@router.get(
    "",
    response_model=list[MessageResponse],
)
async def list_messages(
    db: Session = Depends(get_db),
):
    return get_all_messages(db)