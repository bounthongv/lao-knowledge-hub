from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status

from app.database import supabase
from app.middleware.auth import get_current_user
from app.models.annotations import (
    AnnotationCreate,
    AnnotationResponse,
    AnnotationUpdate,
)

router = APIRouter()


@router.get("/books/{book_id}/annotations", response_model=List[AnnotationResponse])
async def get_annotations(
    book_id: str,
    annotation_type: Optional[str] = None,
    color: Optional[str] = None,
    current_user: dict = Depends(get_current_user),
):
    """
    Get user annotations for a book.
    Requires authentication.
    """
    try:
        query = (
            supabase.table("annotations")
            .select("*")
            .eq("user_id", current_user["id"])
            .eq("book_id", book_id)
        )

        if annotation_type:
            query = query.eq("annotation_type", annotation_type)

        if color:
            query = query.eq("color", color)

        result = query.execute()
        return result.data

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@router.post("/annotations", response_model=AnnotationResponse)
async def create_annotation(
    annotation: AnnotationCreate, current_user: dict = Depends(get_current_user)
):
    """
    Create annotation.
    Requires authentication.
    """
    try:
        data = {
            "user_id": current_user["id"],
            "book_id": annotation.book_id,
            "page_number": annotation.page_number,
            "annotation_type": annotation.annotation_type.value,
            "content": annotation.content,
            "color": annotation.color.value if annotation.color else None,
            "position_data": annotation.position_data,
            "tags": annotation.tags,
        }

        result = supabase.table("annotations").insert(data).execute()
        return result.data[0]

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@router.put("/annotations/{annotation_id}", response_model=AnnotationResponse)
async def update_annotation(
    annotation_id: str,
    annotation: AnnotationUpdate,
    current_user: dict = Depends(get_current_user),
):
    """
    Update annotation.
    Requires authentication.
    """
    try:
        data = {k: v for k, v in annotation.model_dump().items() if v is not None}

        result = (
            supabase.table("annotations")
            .update(data)
            .eq("id", annotation_id)
            .eq("user_id", current_user["id"])
            .execute()
        )

        if not result.data:
            raise HTTPException(status_code=404, detail="Annotation not found")

        return result.data[0]

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@router.delete("/annotations/{annotation_id}")
async def delete_annotation(
    annotation_id: str, current_user: dict = Depends(get_current_user)
):
    """
    Delete annotation.
    Requires authentication.
    """
    try:
        result = (
            supabase.table("annotations")
            .delete()
            .eq("id", annotation_id)
            .eq("user_id", current_user["id"])
            .execute()
        )

        if not result.data:
            raise HTTPException(status_code=404, detail="Annotation not found")

        return {"message": "Annotation deleted"}

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
