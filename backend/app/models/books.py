from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum

class BookStatus(str, Enum):
    """Book status enum"""
    DRAFT = "draft"
    PENDING_REVIEW = "pending_review"
    PUBLISHED = "published"
    REJECTED = "rejected"

class BookCreate(BaseModel):
    """Create book request"""
    title_la: str
    title_en: Optional[str] = None
    description_la: str
    description_en: Optional[str] = None
    price_lak: float = Field(..., gt=0, description="Price in LAK")
    rental_price_lak: Optional[float] = None
    royalty_percentage: float = Field(default=70.0, ge=0, le=100)
    category_ids: Optional[List[str]] = None
    isbn: Optional[str] = None

class BookUpdate(BaseModel):
    """Update book request (all fields optional)"""
    title_la: Optional[str] = None
    title_en: Optional[str] = None
    description_la: Optional[str] = None
    description_en: Optional[str] = None
    price_lak: Optional[float] = None
    rental_price_lak: Optional[float] = None
    
class BookResponse(BaseModel):
    """Book response"""
    id: str
    title_la: str
    title_en: Optional[str] = None
    description_la: Optional[str] = None
    description_en: Optional[str] = None
    author_id: str
    cover_image_url: Optional[str] = None
    price_lak: float
    rental_price_lak: Optional[float] = None
    status: BookStatus
    view_count: int = 0
    purchase_count: int = 0
    rating: Optional[float] = None
    published_at: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class BookListResponse(BaseModel):
    """Paginated book list response"""
    data: List[BookResponse]
    page: int
    limit: int
    total: int
    total_pages: int
