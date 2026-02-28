from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status

from app.database import supabase
from app.middleware.auth import get_current_user, require_professor
from app.models.books import BookCreate, BookResponse, BookUpdate

router = APIRouter()


@router.get("", response_model=List[BookResponse])
async def list_books(
    category: Optional[str] = None,
    search: Optional[str] = None,
    university: Optional[str] = None,
    faculty: Optional[str] = None,
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    sort: str = "published_at",
    order: str = "desc",
):
    """
    List published books with filters and pagination.
    Public endpoint (no authentication required).
    """
    try:
        query = (
            supabase.table("books")
            .select(
                "*, profiles(full_name, avatar_url), book_categories(categories(name_la, name_en, slug))",
                count="exact",
            )
            .eq("status", "published")
        )

        # Apply filters
        if category:
            query = query.eq("book_categories.category_id", category)

        if search:
            query = query.or_(f"title_la.ilike.%{search}%,title_en.ilike.%{search}%")

        # Pagination
        offset = (page - 1) * limit
        response = query.range(offset, offset + limit - 1).execute()

        return response.data

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@router.get("/{book_id}", response_model=BookResponse)
async def get_book(book_id: str):
    """
    Get book details.
    Public endpoint (no authentication required).
    """
    try:
        response = (
            supabase.table("books")
            .select(
                "*, profiles(full_name, avatar_url), chapters(*), book_categories(categories(*)), book_courses(courses(code, name_la))"
            )
            .eq("id", book_id)
            .execute()
        )

        if not response.data:
            raise HTTPException(status_code=404, detail="Book not found")

        # Increment view count
        supabase.rpc("increment_view_count", {"book_id": book_id}).execute()

        return response.data[0]

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@router.get("/{book_id}/sample")
async def get_book_sample(book_id: str):
    """
    Get signed URL for sample pages (first 10 pages).
    Public endpoint (no authentication required).
    """
    try:
        book_response = (
            supabase.table("books").select("file_path").eq("id", book_id).execute()
        )

        if not book_response.data:
            raise HTTPException(status_code=404, detail="Book not found")

        file_path = book_response.data[0]["file_path"]

        # Generate signed URL (1 hour expiry)
        url_response = supabase.storage.from_("book-content").create_signed_url(
            file_path,
            3600,  # 1 hour
        )

        return {
            "signed_url": url_response["signedURL"],
            "expires_in": 3600,
            "sample_pages": 10,
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@router.get("/{book_id}/read")
async def get_full_book(book_id: str, current_user: dict = Depends(get_current_user)):
    """
    Get signed URL for full book (if purchased).
    Requires authentication.
    """
    try:
        # Check if user has purchased
        purchase_response = (
            supabase.table("order_items")
            .select("id, purchase_type, rental_end_date, access_expires_at")
            .eq("book_id", book_id)
            .eq("order.user_id", current_user["id"])
            .execute()
        )

        if not purchase_response.data:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Book not purchased"
            )

        purchase = purchase_response.data[0]

        # Check rental expiry
        if purchase.get("purchase_type") == "rental" and purchase.get(
            "access_expires_at"
        ):
            from datetime import datetime

            if (
                datetime.fromisoformat(
                    purchase["access_expires_at"].replace("Z", "+00:00")
                )
                < datetime.now()
            ):
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN, detail="Rental expired"
                )

        # Get book file path
        book_response = (
            supabase.table("books").select("file_path").eq("id", book_id).execute()
        )
        file_path = book_response.data[0]["file_path"]

        # Generate signed URL (2 hours for reading session)
        url_response = supabase.storage.from_("book-content").create_signed_url(
            file_path,
            7200,  # 2 hours
        )

        return {
            "signed_url": url_response["signedURL"],
            "expires_in": 7200,
            "access_type": purchase.get("purchase_type", "purchase"),
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@router.post("", response_model=BookResponse)
async def create_book(
    book: BookCreate, current_user: dict = Depends(require_professor)
):
    """
    Create a new book (professors only).
    Requires professor role.
    """
    try:
        data = {
            "title_la": book.title_la,
            "title_en": book.title_en,
            "description_la": book.description_la,
            "description_en": book.description_en,
            "author_id": current_user["id"],
            "price_lak": book.price_lak,
            "rental_price_lak": book.rental_price_lak,
            "royalty_percentage": book.royalty_percentage,
            "status": "pending_review",  # Requires admin approval
        }

        response = supabase.table("books").insert(data).execute()
        return response.data[0]

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
