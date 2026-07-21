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

from app.schemas.analysis import AnalysisResponse
from app.services.analysis_service import analyze_message

from app.core.exceptions import (
    AIProviderError,
    AIResponseParseError,
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

@router.post(
    "/{message_id}/analyze",
    response_model=AnalysisResponse,
)
async def analyze(
    message_id: int,
    db: Session = Depends(get_db),
):
    try:
        analysis = await analyze_message(db, message_id)

        if analysis is None:
            raise HTTPException(
                status_code=404,
                detail="Message not found",
            )

        return analysis

    except AIProviderError as exc:
        raise HTTPException(
            status_code=502,
            detail=str(exc),
        ) from exc

    except AIResponseParseError as exc:
        raise HTTPException(
            status_code=500,
            detail=str(exc),
        ) from exc