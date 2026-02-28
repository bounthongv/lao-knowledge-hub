import uuid
from datetime import datetime
from typing import Any, Dict, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel

from app.database import supabase
from app.middleware.auth import get_current_user

router = APIRouter()


class ProgressSyncRequest(BaseModel):
    """Reading progress sync request"""

    book_id: str
    last_page: int
    progress_percentage: float
    time_read_minutes: int = 0


class ProgressResponse(BaseModel):
    """Reading progress response"""

    book_id: str
    last_page: int
    progress_percentage: float
    last_read_at: datetime
    total_time_minutes: int = 0


class StudySessionRequest(BaseModel):
    """Study session request"""

    book_id: str


class StudySessionEndRequest(BaseModel):
    """Study session end request"""

    session_id: str
    pages_read: int = 0
    annotations_created: int = 0


@router.get("/books/{book_id}/progress", response_model=ProgressResponse)
async def get_reading_progress(
    book_id: str, current_user: dict = Depends(get_current_user)
):
    """
    Get reading progress for a book.
    Requires authentication.
    """
    try:
        result = (
            supabase.table("reading_progress")
            .select("*")
            .eq("user_id", current_user["id"])
            .eq("book_id", book_id)
            .execute()
        )

        if not result.data:
            raise HTTPException(status_code=404, detail="Progress not found")

        progress = result.data[0]

        return ProgressResponse(
            book_id=progress["book_id"],
            last_page=progress["last_page"],
            progress_percentage=progress["progress_percentage"],
            last_read_at=progress["last_read_at"],
            total_time_minutes=progress.get("total_time_minutes", 0),
        )

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@router.post("/sync")
async def sync_reading_progress(
    progress: ProgressSyncRequest, current_user: dict = Depends(get_current_user)
):
    """
    Sync reading progress.
    Requires authentication.
    """
    try:
        data = {
            "user_id": current_user["id"],
            "book_id": progress.book_id,
            "last_page": progress.last_page,
            "progress_percentage": progress.progress_percentage,
            "last_read_at": datetime.now().isoformat(),
            "total_time_minutes": progress.time_read_minutes,
        }

        # Upsert (insert or update)
        result = (
            supabase.table("reading_progress")
            .upsert(data, on_conflict="user_id,book_id")
            .execute()
        )

        return {
            "synced": True,
            "last_page": progress.last_page,
            "progress_percentage": progress.progress_percentage,
        }

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@router.post("/start-session")
async def start_study_session(
    session: StudySessionRequest, current_user: dict = Depends(get_current_user)
):
    """
    Start a study session.
    Requires authentication.
    """
    try:
        session_id = str(uuid.uuid4())

        data = {
            "id": session_id,
            "user_id": current_user["id"],
            "book_id": session.book_id,
            "started_at": datetime.now().isoformat(),
        }

        result = supabase.table("study_sessions").insert(data).execute()

        return {"session_id": session_id, "started_at": data["started_at"]}

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@router.post("/end-session")
async def end_study_session(
    session: StudySessionEndRequest, current_user: dict = Depends(get_current_user)
):
    """
    End a study session.
    Requires authentication.
    """
    try:
        # Calculate duration
        session_result = (
            supabase.table("study_sessions")
            .select("started_at")
            .eq("id", session.session_id)
            .execute()
        )

        if not session_result.data:
            raise HTTPException(status_code=404, detail="Session not found")

        started_at = datetime.fromisoformat(
            session_result.data[0]["started_at"].replace("Z", "+00:00")
        )
        ended_at = datetime.now()
        duration_minutes = int((ended_at - started_at).total_seconds() / 60)

        # Update session
        data = {
            "ended_at": ended_at.isoformat(),
            "duration_minutes": duration_minutes,
            "pages_read": session.pages_read,
            "annotations_created": session.annotations_created,
        }

        result = (
            supabase.table("study_sessions")
            .update(data)
            .eq("id", session.session_id)
            .execute()
        )

        return {
            "session_id": session.session_id,
            "ended_at": data["ended_at"],
            "duration_minutes": duration_minutes,
            "pages_read": session.pages_read,
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
