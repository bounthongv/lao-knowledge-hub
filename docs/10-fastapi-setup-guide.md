# FastAPI Backend Setup Guide

**Version:** 1.0  
**Date:** 2026-02-25  
**Purpose:** Step-by-step guide to set up the FastAPI backend

---

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app initialization
│   ├── config.py            # Settings & environment variables
│   ├── database.py          # Supabase client setup
│   ├── models/              # Pydantic models
│   │   ├── __init__.py
│   │   ├── books.py
│   │   ├── orders.py
│   │   ├── users.py
│   │   └── annotations.py
│   ├── routes/              # API routes
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── books.py
│   │   ├── payments.py
│   │   ├── annotations.py
│   │   └── progress.py
│   ├── services/            # Business logic
│   │   ├── __init__.py
│   │   ├── bcel_payment.py
│   │   ├── drm.py
│   │   └── royalties.py
│   └── middleware/          # Custom middleware
│       ├── __init__.py
│       └── auth.py
├── tests/
│   ├── __init__.py
│   ├── test_books.py
│   └── test_orders.py
├── .env
├── .gitignore
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## Step 1: Create Project Structure

### 1.1 Create Directories

```bash
# Create project root
mkdir lao-knowledge-hub-backend
cd lao-knowledge-hub-backend

# Create directory structure
mkdir -p app/models app/routes app/services app/middleware tests

# Create __init__.py files
touch app/__init__.py
touch app/models/__init__.py
touch app/routes/__init__.py
touch app/services/__init__.py
touch app/middleware/__init__.py
touch tests/__init__.py
```

### 1.2 Create requirements.txt

```txt
# FastAPI
fastapi==0.109.0
uvicorn[standard]==0.27.0
python-multipart==0.0.6

# Supabase
supabase==2.3.4
postgrest==0.16.0
gotrue==2.4.0

# Security
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-dotenv==1.0.0

# HTTP Client
httpx==0.26.0
aiohttp==3.9.1

# Validation
pydantic==2.5.3
pydantic-settings==2.1.0
email-validator==2.1.0

# Testing
pytest==7.4.4
pytest-asyncio==0.23.3
httpx==0.26.0

# Utilities
python-dateutil==2.8.2
pytz==2023.3

# Production
gunicorn==21.2.0
```

### 1.3 Create .env File

```bash
# Supabase Configuration
SUPABASE_URL="https://your-project.supabase.co"
SUPABASE_ANON_KEY="your-anon-key"
SUPABASE_SERVICE_KEY="your-service-role-key"

# JWT Settings
JWT_SECRET="your-super-secret-jwt-key-change-this-in-production"
JWT_ALGORITHM="HS256"
JWT_EXPIRATION_MINUTES=60

# BCEL Payment
BCEL_MERCHANT_ID="your-merchant-id"
BCEL_SECRET_KEY="your-bcel-secret"
BCEL_API_URL="https://bcel-payment-api.com"

# Application Settings
APP_NAME="Lao Knowledge Hub API"
DEBUG=true
CORS_ORIGINS="http://localhost:3000,http://localhost:8080"

# Storage
MAX_FILE_SIZE_MB=50
SAMPLE_PAGES=10
```

### 1.4 Create .gitignore

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Environment
.env
.env.local
.env.*.local

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# Testing
.pytest_cache/
.coverage
htmlcov/

# Logs
*.log
```

---

## Step 2: Create Core Files

### 2.1 app/config.py

```python
from pydantic_settings import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    # Supabase
    supabase_url: str
    supabase_anon_key: str
    supabase_service_key: str
    
    # JWT
    jwt_secret: str = "your-super-secret-jwt-key-change-this-in-production"
    jwt_algorithm: str = "HS256"
    jwt_expiration_minutes: int = 60
    
    # BCEL Payment
    bcel_merchant_id: str = ""
    bcel_secret_key: str = ""
    bcel_api_url: str = "https://bcel-payment-api.com"
    
    # Application
    app_name: str = "Lao Knowledge Hub API"
    debug: bool = True
    cors_origins: str = "http://localhost:3000,http://localhost:8080"
    
    # Storage
    max_file_size_mb: int = 50
    sample_pages: int = 10
    
    @property
    def cors_origins_list(self) -> List[str]:
        return [origin.strip() for origin in self.cors_origins.split(",")]
    
    @property
    def max_file_size_bytes(self) -> int:
        return self.max_file_size_mb * 1024 * 1024
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
```

### 2.2 app/database.py

```python
from supabase import create_client, Client
from app.config import settings

# Supabase client for general operations
supabase: Client = create_client(
    settings.supabase_url,
    settings.supabase_service_key
)

# Supabase client for auth operations (uses anon key for client-side auth)
supabase_auth: Client = create_client(
    settings.supabase_url,
    settings.supabase_anon_key
)

def get_supabase() -> Client:
    """Dependency for getting Supabase client"""
    return supabase
```

### 2.3 app/main.py

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routes import auth, books, payments, annotations, progress
import time

# Create FastAPI app
app = FastAPI(
    title=settings.app_name,
    description="API for Lao Knowledge Hub - Digital Publication Platform",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])
app.include_router(books.router, prefix="/api/v1/books", tags=["Books"])
app.include_router(payments.router, prefix="/api/v1/payments", tags=["Payments"])
app.include_router(annotations.router, prefix="/api/v1", tags=["Annotations"])
app.include_router(progress.router, prefix="/api/v1/progress", tags=["Reading Progress"])

# Health check endpoint
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "version": "1.0.0"
    }

# Root endpoint
@app.get("/")
def root():
    return {
        "message": "Welcome to Lao Knowledge Hub API",
        "docs": "/docs",
        "health": "/health"
    }

# Startup event
@app.on_event("startup")
async def startup_event():
    print(f"🚀 Starting {settings.app_name}...")
    print(f"📚 API Documentation: /docs")
    print(f"❤️  Health Check: /health")

# Shutdown event
@app.on_event("shutdown")
async def shutdown_event():
    print("👋 Shutting down...")
```

---

## Step 3: Create Pydantic Models

### 3.1 app/models/users.py

```python
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime
from enum import Enum

class UserRole(str, Enum):
    STUDENT = "student"
    PROFESSOR = "professor"
    ADMIN = "admin"

class DeviceType(str, Enum):
    MOBILE = "mobile"
    TABLET = "tablet"
    WEB = "web"
    DESKTOP = "desktop"

# Request Models
class UserRegister(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)
    full_name: str
    phone: Optional[str] = None
    role: UserRole = UserRole.STUDENT

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class DeviceRegister(BaseModel):
    device_fingerprint: str
    device_name: str
    device_type: DeviceType

# Response Models
class UserProfile(BaseModel):
    id: str
    email: str
    full_name: str
    phone: Optional[str] = None
    role: UserRole
    avatar_url: Optional[str] = None
    is_verified: bool = False
    created_at: datetime
    
    class Config:
        from_attributes = True

class DeviceInfo(BaseModel):
    id: str
    device_name: str
    device_type: DeviceType
    last_active_at: datetime
```

### 3.2 app/models/books.py

```python
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum

class BookStatus(str, Enum):
    DRAFT = "draft"
    PENDING_REVIEW = "pending_review"
    PUBLISHED = "published"
    REJECTED = "rejected"

class BookCreate(BaseModel):
    title_la: str
    title_en: Optional[str] = None
    description_la: str
    description_en: Optional[str] = None
    price_lak: float = Field(..., gt=0)
    rental_price_lak: Optional[float] = None
    royalty_percentage: float = Field(default=70.0, ge=0, le=100)
    category_ids: Optional[List[str]] = None
    isbn: Optional[str] = None

class BookUpdate(BaseModel):
    title_la: Optional[str] = None
    title_en: Optional[str] = None
    description_la: Optional[str] = None
    description_en: Optional[str] = None
    price_lak: Optional[float] = None
    rental_price_lak: Optional[float] = None
    
class BookResponse(BaseModel):
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
```

### 3.3 app/models/orders.py

```python
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime, date
from enum import Enum

class PaymentMethod(str, Enum):
    BCEL_ONE = "bcel_one"
    BANK_TRANSFER = "bank_transfer"
    TELECOM = "telecom"
    CREDIT = "credit"

class PaymentStatus(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    REFUNDED = "refunded"

class PurchaseType(str, Enum):
    PURCHASE = "purchase"
    RENTAL = "rental"

class CheckoutItem(BaseModel):
    book_id: str
    purchase_type: PurchaseType = PurchaseType.PURCHASE

class CheckoutRequest(BaseModel):
    items: List[CheckoutItem]
    payment_method: PaymentMethod
    return_url: str

class OrderResponse(BaseModel):
    id: str
    order_number: str
    total_amount: float
    payment_status: PaymentStatus
    payment_method: PaymentMethod
    items_count: int
    created_at: datetime
    
    class Config:
        from_attributes = True
```

### 3.4 app/models/annotations.py

```python
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum

class AnnotationType(str, Enum):
    HIGHLIGHT = "highlight"
    NOTE = "note"
    BOOKMARK = "bookmark"
    DRAWING = "drawing"

class AnnotationColor(str, Enum):
    YELLOW = "yellow"
    GREEN = "green"
    PINK = "pink"
    BLUE = "blue"
    ORANGE = "orange"

class AnnotationCreate(BaseModel):
    book_id: str
    page_number: int = Field(..., gt=0)
    annotation_type: AnnotationType
    content: Optional[str] = None
    color: Optional[AnnotationColor] = None
    position_data: Optional[Dict[str, Any]] = None
    tags: Optional[List[str]] = None

class AnnotationUpdate(BaseModel):
    content: Optional[str] = None
    color: Optional[AnnotationColor] = None
    tags: Optional[List[str]] = None

class AnnotationResponse(BaseModel):
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
```

---

## Step 4: Create Authentication Middleware

### app/middleware/auth.py

```python
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from supabase import Client
from app.database import supabase, supabase_auth
from app.config import settings
from typing import Optional
import jwt

security = HTTPBearer()

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
) -> dict:
    """
    Verify Supabase JWT and return user info.
    Raises HTTPException if authentication fails.
    """
    token = credentials.credentials
    
    try:
        # Verify JWT with Supabase
        user_response = supabase_auth.auth.get_user(token)
        user = user_response.user
        
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication"
            )
        
        # Get user profile from database
        profile_response = supabase.table("profiles").select("*").eq("id", user.id).execute()
        
        if not profile_response.data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Profile not found"
            )
        
        return profile_response.data[0]
    
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Authentication error: {str(e)}"
        )

async def get_current_user_optional(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(HTTPBearer(auto_error=False))
) -> Optional[dict]:
    """
    Get current user if authenticated, otherwise return None.
    Doesn't raise exception for missing token.
    """
    if not credentials:
        return None
    
    try:
        return await get_current_user(credentials)
    except HTTPException:
        return None

async def require_professor(current_user: dict = Depends(get_current_user)) -> dict:
    """
    Ensure current user is a professor.
    """
    if current_user.get("role") != "professor":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only professors can perform this action"
        )
    return current_user

async def require_admin(current_user: dict = Depends(get_current_user)) -> dict:
    """
    Ensure current user is an admin.
    """
    if current_user.get("role") != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
    return current_user
```

---

## Step 5: Create API Routes

### 5.1 app/routes/auth.py

```python
from fastapi import APIRouter, Depends, HTTPException, status
from app.middleware.auth import get_current_user
from app.models.users import UserRegister, UserLogin, DeviceRegister, UserProfile, DeviceInfo
from app.database import supabase

router = APIRouter()

@router.post("/me", response_model=UserProfile)
async def get_current_user_profile(current_user: dict = Depends(get_current_user)):
    """Get current user profile"""
    return current_user

@router.post("/devices/register", response_model=DeviceInfo)
async def register_device(
    device: DeviceRegister,
    current_user: dict = Depends(get_current_user)
):
    """Register device for DRM (max 3 devices per user)"""
    try:
        # Check device limit
        existing_devices = supabase.table("user_devices").select("id").eq("user_id", current_user["id"]).execute()
        
        if len(existing_devices.data) >= 3:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Device limit reached (max 3 devices)"
            )
        
        # Register device
        result = supabase.table("user_devices").insert({
            "user_id": current_user["id"],
            "device_fingerprint": device.device_fingerprint,
            "device_name": device.device_name,
            "device_type": device.device_type.value
        }).execute()
        
        return result.data[0]
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.get("/devices", response_model=list[DeviceInfo])
async def list_devices(current_user: dict = Depends(get_current_user)):
    """List registered devices"""
    result = supabase.table("user_devices").select("*").eq("user_id", current_user["id"]).execute()
    return result.data

@router.delete("/devices/{device_id}")
async def remove_device(
    device_id: str,
    current_user: dict = Depends(get_current_user)
):
    """Remove a registered device"""
    result = supabase.table("user_devices").delete().eq("id", device_id).eq("user_id", current_user["id"]).execute()
    
    if not result.data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Device not found"
        )
    
    return {"message": "Device removed successfully"}
```

### 5.2 app/routes/books.py

```python
from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional
from app.middleware.auth import get_current_user, require_professor
from app.models.books import BookCreate, BookUpdate, BookResponse
from app.database import supabase

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
    order: str = "desc"
):
    """List published books with filters and pagination"""
    try:
        query = supabase.table("books").select(
            "*, profiles(full_name, avatar_url), book_categories(categories(name_la, name_en, slug))",
            count="exact"
        ).eq("status", "published")
        
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
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.get("/{book_id}", response_model=BookResponse)
async def get_book(book_id: str):
    """Get book details"""
    try:
        response = supabase.table("books").select(
            "*, profiles(full_name, avatar_url), chapters(*), book_categories(categories(*)), book_courses(courses(code, name_la))"
        ).eq("id", book_id).execute()
        
        if not response.data:
            raise HTTPException(status_code=404, detail="Book not found")
        
        # Increment view count
        supabase.rpc("increment_view_count", {"book_id": book_id}).execute()
        
        return response.data[0]
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.get("/{book_id}/sample")
async def get_book_sample(book_id: str):
    """Get signed URL for sample pages (first 10 pages)"""
    try:
        book_response = supabase.table("books").select("file_path").eq("id", book_id).execute()
        
        if not book_response.data:
            raise HTTPException(status_code=404, detail="Book not found")
        
        file_path = book_response.data[0]["file_path"]
        
        # Generate signed URL (1 hour expiry)
        url_response = supabase.storage.from_("book-content").create_signed_url(
            file_path,
            3600  # 1 hour
        )
        
        return {
            "signed_url": url_response["signedURL"],
            "expires_in": 3600,
            "sample_pages": 10
        }
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.get("/{book_id}/read")
async def get_full_book(
    book_id: str,
    current_user: dict = Depends(get_current_user)
):
    """Get signed URL for full book (if purchased)"""
    try:
        # Check if user has purchased
        purchase_response = supabase.table("order_items").select(
            "id, purchase_type, rental_end_date, access_expires_at"
        ).eq("book_id", book_id).eq("order.user_id", current_user["id"]).execute()
        
        if not purchase_response.data:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Book not purchased"
            )
        
        purchase = purchase_response.data[0]
        
        # Check rental expiry
        if purchase.get("purchase_type") == "rental" and purchase.get("access_expires_at"):
            from datetime import datetime
            if datetime.fromisoformat(purchase["access_expires_at"].replace('Z', '+00:00')) < datetime.now():
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Rental expired"
                )
        
        # Get book file path
        book_response = supabase.table("books").select("file_path").eq("id", book_id).execute()
        file_path = book_response.data[0]["file_path"]
        
        # Generate signed URL (2 hours for reading session)
        url_response = supabase.storage.from_("book-content").create_signed_url(
            file_path,
            7200  # 2 hours
        )
        
        return {
            "signed_url": url_response["signedURL"],
            "expires_in": 7200,
            "access_type": purchase.get("purchase_type", "purchase")
        }
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.post("", response_model=BookResponse)
async def create_book(
    book: BookCreate,
    current_user: dict = Depends(require_professor)
):
    """Create a new book (professors only)"""
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
            "status": "pending_review"  # Requires admin approval
        }
        
        response = supabase.table("books").insert(data).execute()
        return response.data[0]
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
```

### 5.3 app/routes/annotations.py

```python
from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional
from app.middleware.auth import get_current_user
from app.models.annotations import AnnotationCreate, AnnotationUpdate, AnnotationResponse
from app.database import supabase

router = APIRouter()

@router.get("/books/{book_id}/annotations", response_model=List[AnnotationResponse])
async def get_annotations(
    book_id: str,
    annotation_type: Optional[str] = None,
    color: Optional[str] = None,
    current_user: dict = Depends(get_current_user)
):
    """Get user annotations for a book"""
    try:
        query = supabase.table("annotations").select("*").eq("user_id", current_user["id"]).eq("book_id", book_id)
        
        if annotation_type:
            query = query.eq("annotation_type", annotation_type)
        
        if color:
            query = query.eq("color", color)
        
        result = query.execute()
        return result.data
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.post("/annotations", response_model=AnnotationResponse)
async def create_annotation(
    annotation: AnnotationCreate,
    current_user: dict = Depends(get_current_user)
):
    """Create annotation"""
    try:
        data = {
            "user_id": current_user["id"],
            "book_id": annotation.book_id,
            "page_number": annotation.page_number,
            "annotation_type": annotation.annotation_type.value,
            "content": annotation.content,
            "color": annotation.color.value if annotation.color else None,
            "position_data": annotation.position_data,
            "tags": annotation.tags
        }
        
        result = supabase.table("annotations").insert(data).execute()
        return result.data[0]
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.put("/annotations/{annotation_id}", response_model=AnnotationResponse)
async def update_annotation(
    annotation_id: str,
    annotation: AnnotationUpdate,
    current_user: dict = Depends(get_current_user)
):
    """Update annotation"""
    try:
        data = {k: v for k, v in annotation.model_dump().items() if v is not None}
        
        result = supabase.table("annotations").update(data).eq("id", annotation_id).eq("user_id", current_user["id"]).execute()
        
        if not result.data:
            raise HTTPException(status_code=404, detail="Annotation not found")
        
        return result.data[0]
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.delete("/annotations/{annotation_id}")
async def delete_annotation(
    annotation_id: str,
    current_user: dict = Depends(get_current_user)
):
    """Delete annotation"""
    try:
        result = supabase.table("annotations").delete().eq("id", annotation_id).eq("user_id", current_user["id"]).execute()
        
        if not result.data:
            raise HTTPException(status_code=404, detail="Annotation not found")
        
        return {"message": "Annotation deleted"}
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
```

---

## Step 6: Run and Test

### 6.1 Install Dependencies

```bash
cd lao-knowledge-hub-backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 6.2 Run Development Server

```bash
# Run with uvicorn
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 6.3 Test API

Open your browser:
- **API Docs:** http://localhost:8000/docs
- **Health Check:** http://localhost:8000/health
- **Root:** http://localhost:8000/

### 6.4 Test with curl

```bash
# Health check
curl http://localhost:8000/health

# List books (should be empty initially)
curl http://localhost:8000/api/v1/books
```

---

## Step 7: Docker Deployment (Optional)

### Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Run with gunicorn for production
CMD ["gunicorn", "app.main:app", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
```

### docker-compose.yml

```yaml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "8000:8000"
    env_file:
      - .env
    restart: unless-stopped
```

---

## Next Steps

✅ **FastAPI Backend Setup Complete!**

Now proceed to:

1. **Implement remaining routes** - payments, progress, reviews
2. **Set up Flutter app** → See `docs/10-flutter-setup-guide.md`
3. **Configure BCEL Payment** - Contact BCEL for API credentials
4. **Deploy to Firebase Cloud Run** or similar

---

## Troubleshooting

### Issue: Module not found

```
ModuleNotFoundError: No module named 'app'
```

**Solution:** Make sure you're running from the project root and `__init__.py` files exist.

### Issue: Supabase connection error

```
Error connecting to Supabase
```

**Solution:** Check your `.env` file has correct Supabase URL and keys.

### Issue: CORS error

```
CORS policy blocked request
```

**Solution:** Add your frontend URL to `CORS_ORIGINS` in `.env`.
