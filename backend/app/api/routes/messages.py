from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.message import MessageResponse
from app.services.message_service import get_all_messages

from fastapi import HTTPException
from app.services.message_service import (
    get_all_messages,
    get_message_by_id,
)

router = APIRouter(prefix="/messages", tags=["Messages"])


@router.get("",response_model=list[MessageResponse],)
async def list_messages(
    db: Session = Depends(get_db),
):
    return get_all_messages(db)

@router.get("/{message_id}", response_model=MessageResponse)
def get_message(message_id: int, db: Session = Depends(get_db)):
    message = get_message_by_id(db, message_id)

    if message is None:
        raise HTTPException(
            status_code=404,
            detail="No Messages available for the given ID.",
        )

    return message