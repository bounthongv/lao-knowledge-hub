from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum

class AnnotationType(str, Enum):
    """Annotation type enum"""
    HIGHLIGHT = "highlight"
    NOTE = "note"
    BOOKMARK = "bookmark"
    DRAWING = "drawing"

class AnnotationColor(str, Enum):
    """Annotation color enum"""
    YELLOW = "yellow"
    GREEN = "green"
    PINK = "pink"
    BLUE = "blue"
    ORANGE = "orange"

class AnnotationCreate(BaseModel):
    """Create annotation request"""
    book_id: str
    page_number: int = Field(..., gt=0)
    annotation_type: AnnotationType
    content: Optional[str] = None
    color: Optional[AnnotationColor] = None
    position_data: Optional[Dict[str, Any]] = None
    tags: Optional[List[str]] = None

class AnnotationUpdate(BaseModel):
    """Update annotation request"""
    content: Optional[str] = None
    color: Optional[AnnotationColor] = None
    tags: Optional[List[str]] = None

class AnnotationResponse(BaseModel):
    """Annotation response"""
    id: str
    book_id: str
    page_number: int
    annotation_type: AnnotationType
    content: Optional[str] = None
    color: Optional[AnnotationColor] = None
    position_data: Optional[Dict[str, Any]] = None
    tags: Optional[List[str]] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
