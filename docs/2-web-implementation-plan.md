# Web Implementation Plan: Lao Knowledge Hub

## Executive Summary

This document outlines the technical implementation plan for the Lao Knowledge Hub web platform—a digital publication and e-learning platform tailored for Laos. The plan prioritizes rapid MVP delivery while maintaining scalability for future growth.

---

## 1. Technology Stack

### 1.1 Core Stack Recommendation

| Layer | Technology | Rationale |
|-------|------------|-----------|
| **Client (Web + Mobile)** | Flutter | Single codebase for iOS, Android, and Web; reduces development time by 50%+ |
| **Public Web (SEO)** | Next.js 14+ (React) | SSR/SSG for SEO—book listings, descriptions indexed by Google |
| **Backend Framework** | Python + FastAPI | Fast, modern, async-ready; comfortable for team |
| **Backend-as-a-Service** | Supabase | PostgreSQL, Auth, Storage, Realtime out-of-the-box; reduces boilerplate |
| **File Storage** | Supabase Storage | Integrated with Supabase; secure PDF/ePub storage with signed URLs |
| **PDF Rendering** | `syncfusion_flutter_pdfviewer` | Native Flutter PDF viewer with annotation support |
| **Authentication** | Supabase Auth | Multi-provider, JWT-based, row-level security integration |
| **Payments** | BCEL One API + manual fallback | Local payment integration |
| **Hosting** | Firebase Hosting | Free SSL, CDN, easy deployment; works well with Flutter Web |
| **Admin Dashboard** | React Admin + Supabase | Rapid admin panel development with Supabase data provider |

### 1.2 Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                      PUBLIC-FACING LAYER                        │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  Next.js Marketing Site (SEO-optimized)                 │   │
│  │  • Book catalog (indexed by Google)                     │   │
│  │  • Book detail pages                                    │   │
│  │  • Author profiles                                      │   │
│  │  • Landing pages                                        │   │
│  └─────────────────────────────────────────────────────────┘   │
│                          │                                      │
│                          ▼                                      │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  Flutter Web App (Authenticated Users)                  │   │
│  │  • Reader with annotations                              │   │
│  │  • User library                                         │   │
│  │  • Cart & checkout                                      │   │
│  │  • Account management                                   │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                         API LAYER                               │
│              Python + FastAPI (on Firebase Cloud Run)           │
│         Business Logic │ Payment Processing │ DRM               │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      SUPABASE LAYER                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐  │
│  │  PostgreSQL  │  │     Auth     │  │      Storage         │  │
│  │              │  │              │  │                      │  │
│  │ • Users      │  │ • JWT        │  │ • PDF Files          │  │
│  │ • Books      │  │ • Sessions   │  │ • Cover Images       │  │
│  │ • Orders     │  │ • RLS        │  │ • Encrypted Content  │  │
│  │ • Royalties  │  │              │  │                      │  │
│  └──────────────┘  └──────────────┘  └──────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    ADMIN DASHBOARD                              │
│           React Admin + Supabase Data Provider                  │
│  • Book review & approval  • User management  • Analytics       │
└─────────────────────────────────────────────────────────────────┘
```

### 1.3 Why This Hybrid Approach?

| Concern | Solution |
|---------|----------|
| **SEO for book discovery** | Next.js handles public pages (SSR/SSG for Google indexing) |
| **Single codebase for app** | Flutter for authenticated user experience (web + mobile) |
| **Rapid backend development** | Supabase provides 80% of backend out-of-the-box |
| **Custom business logic** | FastAPI for payments, DRM, royalties, complex queries |
| **Low ops overhead** | Firebase Hosting + Supabase managed services |

### 1.4 Alternative Stack (If Requirements Change)

| If Team Knows... | Use Instead |
|------------------|-------------|
| Node.js | Express/NestJS instead of FastAPI |
| .NET | ASP.NET Core + Supabase |
| PHP | Laravel + Supabase (via REST) |

---

## 2. Supabase Database Schema

### 2.1 Enable Required Extensions

```sql
-- Run in Supabase SQL Editor
create extension if not exists "uuid-ossp";
create extension if not exists "pgcrypto";
```

### 2.2 Users & Authentication

Supabase Auth handles users automatically. We extend with profiles:

```sql
-- Profiles table (extends Supabase auth.users)
create table profiles (
    id uuid references auth.users on delete cascade primary key,
    full_name text not null,
    phone text,
    role text default 'student' check (role in ('student', 'professor', 'admin')),
    avatar_url text,
    is_verified boolean default false,
    created_at timestamptz default now(),
    updated_at timestamptz default now()
);

-- User devices (for DRM limiting)
create table user_devices (
    id uuid default uuid_generate_v4() primary key,
    user_id uuid references profiles(id) on delete cascade,
    device_fingerprint text not null,
    device_name text,
    last_active_at timestamptz default now(),
    unique(user_id, device_fingerprint)
);

-- Row Level Security (RLS)
alter table profiles enable row level security;

-- Users can view their own profile
create policy "Users can view own profile"
    on profiles for select
    using (auth.uid() = id);

-- Users can update their own profile
create policy "Users can update own profile"
    on profiles for update
    using (auth.uid() = id);

-- Professors can view other professors (for directory)
create policy "Professors can view other professors"
    on profiles for select
    using (role = 'professor');
```

### 2.3 Content Management

```sql
-- Books table
create table books (
    id uuid default uuid_generate_v4() primary key,
    title_la text not null,
    title_en text,
    description_la text,
    description_en text,
    author_id uuid references profiles(id) not null,
    cover_image_url text,
    file_path text not null,
    file_hash text not null,
    isbn text,
    price_lak numeric(10,2) not null,
    rental_price_lak numeric(10,2),
    royalty_percentage numeric(5,2) default 70.00,
    status text default 'draft' check (status in ('draft', 'pending_review', 'published', 'rejected')),
    view_count integer default 0,
    purchase_count integer default 0,
    created_at timestamptz default now(),
    updated_at timestamptz default now()
);

-- Chapters (for TOC navigation)
create table chapters (
    id uuid default uuid_generate_v4() primary key,
    book_id uuid references books(id) on delete cascade,
    title_la text not null,
    title_en text,
    page_start integer not null,
    page_end integer not null,
    sort_order integer not null,
    unique(book_id, sort_order)
);

-- Categories/Subjects
create table categories (
    id uuid default uuid_generate_v4() primary key,
    name_la text not null,
    name_en text,
    slug text unique not null,
    parent_id uuid references categories(id)
);

create table book_categories (
    book_id uuid references books(id) on delete cascade,
    category_id uuid references categories(id) on delete cascade,
    primary key (book_id, category_id)
);

-- RLS for books
alter table books enable row level security;

-- Everyone can view published books
create policy "Anyone can view published books"
    on books for select
    using (status = 'published');

-- Professors can create books
create policy "Professors can create books"
    on books for insert
    with check (auth.uid() = author_id);

-- Authors can update their own books
create policy "Authors can update own books"
    on books for update
    using (auth.uid() = author_id);

-- Admins can view all books (via service role)
```

### 2.4 Purchases & Royalties

```sql
-- Orders
create table orders (
    id uuid default uuid_generate_v4() primary key,
    user_id uuid references profiles(id) not null,
    total_amount numeric(10,2) not null,
    payment_method text check (payment_method in ('bcel_one', 'bank_transfer', 'telecom')),
    payment_status text default 'pending' check (payment_status in ('pending', 'completed', 'failed', 'refunded')),
    bcel_transaction_id text,
    created_at timestamptz default now(),
    updated_at timestamptz default now()
);

-- Order items
create table order_items (
    id uuid default uuid_generate_v4() primary key,
    order_id uuid references orders(id) on delete cascade,
    book_id uuid references books(id) on delete cascade,
    price_at_purchase numeric(10,2) not null,
    royalty_amount numeric(10,2) not null,
    purchase_type text default 'purchase' check (purchase_type in ('purchase', 'rental')),
    rental_end_date timestamptz,
    created_at timestamptz default now()
);

-- Royalty tracking
create table royalty_statements (
    id uuid default uuid_generate_v4() primary key,
    author_id uuid references profiles(id) not null,
    period_start date not null,
    period_end date not null,
    total_sales numeric(10,2) not null,
    total_royalty numeric(10,2) not null,
    status text default 'pending' check (status in ('pending', 'paid')),
    paid_at timestamptz,
    created_at timestamptz default now()
);

create table royalty_line_items (
    id uuid default uuid_generate_v4() primary key,
    statement_id uuid references royalty_statements(id) on delete cascade,
    book_id uuid references books(id) on delete cascade,
    order_item_id uuid references order_items(id),
    sale_amount numeric(10,2) not null,
    royalty_amount numeric(10,2) not null,
    sale_date timestamptz default now()
);

-- RLS for orders
alter table orders enable row level security;

create policy "Users can view own orders"
    on orders for select
    using (auth.uid() = user_id);

create policy "Users can create own orders"
    on orders for insert
    with check (auth.uid() = user_id);
```

### 2.5 Annotations & Study Tools

```sql
-- User annotations (highlights, notes)
create table annotations (
    id uuid default uuid_generate_v4() primary key,
    user_id uuid references profiles(id) on delete cascade,
    book_id uuid references books(id) on delete cascade,
    page_number integer not null,
    annotation_type text not null check (annotation_type in ('highlight', 'note', 'bookmark')),
    content text,
    color text check (color in ('yellow', 'green', 'pink', 'blue')),
    position_data jsonb,
    created_at timestamptz default now(),
    updated_at timestamptz default now()
);

-- Reading progress
create table reading_progress (
    user_id uuid references profiles(id) on delete cascade,
    book_id uuid references books(id) on delete cascade,
    last_page integer not null,
    progress_percentage numeric(5,2) default 0,
    last_read_at timestamptz default now(),
    primary key (user_id, book_id)
);

-- RLS for annotations
alter table annotations enable row level security;

create policy "Users can view own annotations"
    on annotations for select
    using (auth.uid() = user_id);

create policy "Users can create own annotations"
    on annotations for insert
    with check (auth.uid() = user_id);

create policy "Users can update own annotations"
    on annotations for update
    using (auth.uid() = user_id);

create policy "Users can delete own annotations"
    on annotations for delete
    using (auth.uid() = user_id);
```

### 2.6 Supabase Storage Buckets

```sql
-- Create storage buckets via Supabase dashboard or API:
-- 1. 'book-covers' (public)
-- 2. 'book-content' (private, signed URLs only)

-- Storage policies
-- Allow authenticated users to upload covers
create policy "Professors can upload covers"
    on storage.objects for insert
    with check (
        bucket_id = 'book-covers' and
        auth.uid()::text = (storage.foldername(name))[1]
    );

-- Allow public read on covers
create policy "Anyone can view covers"
    on storage.objects for select
    using (bucket_id = 'book-covers');

-- Only service role can access book content
-- (FastAPI backend handles signed URL generation)
```

### 2.7 Database Functions & Triggers

```sql
-- Auto-create profile on user signup
create or replace function public.handle_new_user()
returns trigger as $$
begin
    insert into public.profiles (id, full_name, email, role)
    values (
        new.id,
        new.raw_user_meta_data->>'full_name',
        new.email,
        coalesce(new.raw_user_meta_data->>'role', 'student')
    );
    return new;
end;
$$ language plpgsql security definer;

create trigger on_auth_user_created
    after insert on auth.users
    for each row execute procedure public.handle_new_user();

-- Update book view count
create or replace function increment_view_count()
returns trigger as $$
begin
    update books set view_count = view_count + 1
    where id = new.book_id;
    return new;
end;
$$ language plpgsql;

-- Auto-update updated_at timestamp
create or replace function update_updated_at_column()
returns trigger as $$
begin
    new.updated_at = now();
    return new;
end;
$$ language plpgsql;

create trigger books_updated_at before update on books
    for each row execute procedure update_updated_at_column();
```

---

## 3. API Endpoints (FastAPI)

### 3.1 Project Structure

```
backend/
├── app/
│   ├── main.py              # FastAPI app initialization
│   ├── config.py            # Settings & environment
│   ├── database.py          # Supabase client setup
│   ├── models/              # Pydantic models
│   │   ├── books.py
│   │   ├── orders.py
│   │   └── users.py
│   ├── routes/              # API routes
│   │   ├── auth.py
│   │   ├── books.py
│   │   ├── payments.py
│   │   └── annotations.py
│   ├── services/            # Business logic
│   │   ├── bcel_payment.py
│   │   ├── drm.py
│   │   └── royalties.py
│   └── middleware/          # Custom middleware
├── requirements.txt
└── Dockerfile
```

### 3.2 Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/login` | Exchange Supabase token for session |
| POST | `/api/auth/verify` | Verify Supabase JWT |
| GET | `/api/auth/me` | Get current user profile |
| POST | `/api/auth/devices/register` | Register device for DRM |

### 3.3 Books & Content

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/books` | List books (filters, pagination) |
| GET | `/api/books/:id` | Get book details |
| GET | `/api/books/:id/sample` | Get signed sample pages URL |
| GET | `/api/books/:id/read` | Get signed full book URL (if purchased) |
| POST | `/api/books` | Create book (professors) |
| PUT | `/api/books/:id` | Update book |
| DELETE | `/api/books/:id` | Delete book |
| GET | `/api/books/:id/chapters` | Get chapter list |

### 3.4 Annotations

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/books/:id/annotations` | Get user annotations |
| POST | `/api/annotations` | Create annotation |
| PUT | `/api/annotations/:id` | Update annotation |
| DELETE | `/api/annotations/:id` | Delete annotation |

### 3.5 Purchases & Payments

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/cart/checkout` | Create order + initiate payment |
| GET | `/api/orders` | Get user orders |
| GET | `/api/orders/:id` | Get order details |
| POST | `/api/payments/bcel/initiate` | Initiate BCEL payment |
| POST | `/api/payments/bcel/callback` | BCEL payment callback |
| GET | `/api/royalties/statement` | Get royalty statement (authors) |

### 3.6 Admin

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/admin/books` | List all books (admin) |
| PUT | `/api/admin/books/:id/review` | Review/approve book |
| GET | `/api/admin/users` | List users |
| GET | `/api/admin/analytics` | Get platform analytics |

---

## 4. FastAPI Backend Implementation

### 4.1 Setup & Configuration

```python
# app/main.py
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from supabase import create_client, Client
from app.config import settings
from app.routes import books, payments, annotations, auth

app = FastAPI(title="Lao Knowledge Hub API")

# CORS for Flutter Web + Next.js
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://your-project.web.app",  # Firebase Hosting
        "https://your-project.firebaseapp.com",
        "http://localhost:3000",  # Next.js dev
        "http://localhost:8080",  # Flutter Web dev
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Supabase client
supabase: Client = create_client(
    settings.supabase_url,
    settings.supabase_service_key
)

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(books.router, prefix="/api/books", tags=["books"])
app.include_router(payments.router, prefix="/api/payments", tags=["payments"])
app.include_router(annotations.router, prefix="/api", tags=["annotations"])

@app.get("/health")
def health_check():
    return {"status": "healthy"}
```

```python
# app/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    supabase_url: str
    supabase_service_key: str
    supabase_anon_key: str
    bcel_merchant_id: str
    bcel_secret_key: str
    firebase_credentials: str
    
    class Config:
        env_file = ".env"

settings = Settings()
```

### 4.2 Authentication Middleware

```python
# app/middleware/auth.py
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from supabase import Client
from app.database import supabase
import jwt

security = HTTPBearer()

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
) -> dict:
    """Verify Supabase JWT and return user info"""
    token = credentials.credentials
    
    try:
        # Verify with Supabase
        response = supabase.auth.get_user(token)
        user = response.user
        
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication"
            )
        
        # Get profile from database
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
```

### 4.3 Books API

```python
# app/routes/books.py
from fastapi import APIRouter, Depends, HTTPException, Query
from supabase import Client
from app.database import supabase
from app.middleware.auth import get_current_user
from app.models.books import BookCreate, BookUpdate, BookResponse
from typing import List, Optional
from datetime import datetime

router = APIRouter()

@router.get("", response_model=List[BookResponse])
def list_books(
    category: Optional[str] = None,
    search: Optional[str] = None,
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100)
):
    """List published books with filters"""
    query = supabase.table("books").select(
        "*, profiles(full_name, avatar_url), book_categories(categories(name_la, name_en))"
    ).eq("status", "published")
    
    if category:
        query = query.eq("book_categories.category_id", category)
    
    if search:
        query = query.or_(
            f"title_la.ilike.%{search}%,title_en.ilike.%{search}%"
        )
    
    offset = (page - 1) * limit
    response = query.range(offset, offset + limit - 1).execute()
    
    return response.data

@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: str):
    """Get book details"""
    response = supabase.table("books").select(
        "*, profiles(full_name, avatar_url), chapters(*), book_categories(categories(*))"
    ).eq("id", book_id).execute()
    
    if not response.data:
        raise HTTPException(status_code=404, detail="Book not found")
    
    # Increment view count
    supabase.rpc("increment_view_count", {"book_id": book_id}).execute()
    
    return response.data[0]

@router.post("", response_model=BookResponse)
def create_book(
    book: BookCreate,
    current_user: dict = Depends(get_current_user)
):
    """Create a new book (professors only)"""
    if current_user["role"] != "professor":
        raise HTTPException(
            status_code=403,
            detail="Only professors can create books"
        )
    
    data = {
        "title_la": book.title_la,
        "title_en": book.title_en,
        "description_la": book.description_la,
        "description_en": book.description_en,
        "author_id": current_user["id"],
        "price_lak": book.price_lak,
        "royalty_percentage": book.royalty_percentage,
        "status": "pending_review"  # Requires admin approval
    }
    
    response = supabase.table("books").insert(data).execute()
    return response.data[0]

@router.get("/{book_id}/sample")
def get_sample_pages(book_id: str):
    """Get signed URL for sample pages (first 10 pages)"""
    book_response = supabase.table("books").select("file_path").eq("id", book_id).execute()
    
    if not book_response.data:
        raise HTTPException(status_code=404, detail="Book not found")
    
    file_path = book_response.data[0]["file_path"]
    
    # Generate signed URL (1 hour expiry)
    url_response = supabase.storage.from_("book-content").create_signed_url(
        file_path,
        3600,  # 1 hour
        {"transform": {"pages": "1-10"}}  # Only first 10 pages
    )
    
    return {"signed_url": url_response["signedURL"]}

@router.get("/{book_id}/read")
def get_full_book(
    book_id: str,
    current_user: dict = Depends(get_current_user)
):
    """Get signed URL for full book (if purchased)"""
    # Check if user has purchased
    purchase_response = supabase.table("order_items").select(
        "id, purchase_type, rental_end_date"
    ).eq("book_id", book_id).eq("order.user_id", current_user["id"]).execute()
    
    if not purchase_response.data:
        raise HTTPException(
            status_code=403,
            detail="Book not purchased"
        )
    
    purchase = purchase_response.data[0]
    
    # Check rental expiry
    if purchase["purchase_type"] == "rental" and purchase["rental_end_date"]:
        if datetime.fromisoformat(purchase["rental_end_date"]) < datetime.now():
            raise HTTPException(
                status_code=403,
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
    
    return {"signed_url": url_response["signedURL"]}
```

### 4.4 Payment Service (BCEL)

```python
# app/services/bcel_payment.py
import hashlib
import hmac
import json
from app.config import settings

def generate_bcel_signature(data: dict) -> str:
    """Generate HMAC signature for BCEL API"""
    payload = json.dumps(data, sort_keys=True)
    signature = hmac.new(
        settings.bcel_secret_key.encode(),
        payload.encode(),
        hashlib.sha256
    ).hexdigest()
    return signature

async def initiate_payment(order_id: str, amount: float, return_url: str) -> dict:
    """Initiate BCEL One payment"""
    import aiohttp
    
    payload = {
        "merchant_id": settings.bcel_merchant_id,
        "order_id": order_id,
        "amount": amount,
        "return_url": return_url,
        "cancel_url": return_url.replace("/success", "/cancel"),
        "webhook_url": f"{settings.api_base_url}/api/payments/bcel/callback",
        "timestamp": int(datetime.now().timestamp())
    }
    
    signature = generate_bcel_signature(payload)
    payload["signature"] = signature
    
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://payment.bcel.com.kh/api/v1/payment",
            json=payload
        ) as response:
            return await response.json()

def verify_callback(callback_data: dict) -> bool:
    """Verify BCEL callback signature"""
    received_signature = callback_data.pop("signature", None)
    expected_signature = generate_bcel_signature(callback_data)
    return hmac.compare_digest(received_signature, expected_signature)
```

```python
# app/routes/payments.py
from fastapi import APIRouter, Depends, HTTPException, Request
from app.database import supabase
from app.middleware.auth import get_current_user
from app.services.bcel_payment import initiate_payment, verify_callback
from app.config import settings
from datetime import datetime

router = APIRouter()

@router.post("/bcel/initiate")
async def bcel_initiate(
    order_id: str,
    current_user: dict = Depends(get_current_user)
):
    """Initiate BCEL payment for order"""
    # Get order details
    order_response = supabase.table("orders").select("*").eq("id", order_id).execute()
    
    if not order_response.data:
        raise HTTPException(status_code=404, detail="Order not found")
    
    order = order_response.data[0]
    
    if order["user_id"] != current_user["id"]:
        raise HTTPException(status_code=403, detail="Not your order")
    
    if order["payment_status"] != "pending":
        raise HTTPException(status_code=400, detail="Order already paid")
    
    # Initiate BCEL payment
    payment_data = await initiate_payment(
        order_id=order_id,
        amount=order["total_amount"],
        return_url=f"{settings.frontend_url}/payment/success"
    )
    
    return payment_data

@router.post("/bcel/callback")
async def bcel_callback(request: Request):
    """BCEL payment webhook callback"""
    callback_data = await request.json()
    
    if not verify_callback(callback_data):
        raise HTTPException(status_code=400, detail="Invalid signature")
    
    order_id = callback_data["order_id"]
    status = callback_data["status"]  # "success" or "failed"
    transaction_id = callback_data["transaction_id"]
    
    # Update order status
    if status == "success":
        supabase.table("orders").update({
            "payment_status": "completed",
            "bcel_transaction_id": transaction_id,
            "updated_at": datetime.now().isoformat()
        }).eq("id", order_id).execute()
        
        # Create royalty line items
        # (See royalties service)
    else:
        supabase.table("orders").update({
            "payment_status": "failed"
        }).eq("id", order_id).execute()
    
    return {"status": "ok"}
```

---

## 5. Flutter Client Implementation

### 5.1 Project Structure

```
flutter_app/
├── lib/
│   ├── main.dart                  # App entry point
│   ├── app.dart                   # App widget (routes, theme)
│   ├── config/
│   │   ├── routes.dart            # Route definitions
│   │   ├── theme.dart             # App theme
│   │   └── constants.dart         # App constants
│   ├── core/
│   │   ├── services/              # Global services
│   │   │   ├── supabase_service.dart
│   │   │   ├── auth_service.dart
│   │   │   └── payment_service.dart
│   │   ├── utils/                 # Utilities
│   │   └── widgets/               # Reusable widgets
│   ├── features/
│   │   ├── auth/                  # Authentication
│   │   │   ├── login_screen.dart
│   │   │   ├── register_screen.dart
│   │   │   └── auth_service.dart
│   │   ├── books/                 # Book browsing
│   │   │   ├── book_list_screen.dart
│   │   │   ├── book_detail_screen.dart
│   │   │   ├── book_card.dart
│   │   │   └── book_repository.dart
│   │   ├── reader/                # PDF reader
│   │   │   ├── reader_screen.dart
│   │   │   ├── pdf_viewer.dart
│   │   │   └── annotation_layer.dart
│   │   ├── library/               # User's books
│   │   │   └── library_screen.dart
│   │   ├── cart/                  # Shopping cart
│   │   │   ├── cart_screen.dart
│   │   │   └── checkout_screen.dart
│   │   └── profile/               # User profile
│   │       └── profile_screen.dart
│   └── models/
│       ├── book.dart
│       ├── user.dart
│       ├── order.dart
│       └── annotation.dart
├── pubspec.yaml
└── test/
```

### 5.2 Dependencies (pubspec.yaml)

```yaml
name: lao_knowledge_hub
description: Lao Knowledge Hub - Digital Book Platform
version: 1.0.0+1

environment:
  sdk: '>=3.0.0 <4.0.0'

dependencies:
  flutter:
    sdk: flutter
  
  # Supabase
  supabase_flutter: ^2.0.0
  
  # State Management
  flutter_riverpod: ^2.4.0
  riverpod_annotation: ^2.3.0
  
  # PDF Reader
  syncfusion_flutter_pdfviewer: ^24.0.0
  
  # Navigation
  go_router: ^13.0.0
  
  # HTTP
  dio: ^5.4.0
  
  # Local Storage
  hive_flutter: ^1.1.0
  hive: ^2.2.3
  
  # UI
  flutter_svg: ^2.0.9
  cached_network_image: ^3.3.1
  shimmer: ^3.0.0
  
  # Utilities
  intl: ^0.19.0
  path_provider: ^2.1.2
  url_launcher: ^6.2.4
  device_info_plus: ^10.0.0

dev_dependencies:
  flutter_test:
    sdk: flutter
  flutter_lints: ^3.0.0
  build_runner: ^2.4.8
  riverpod_generator: ^2.3.0

flutter:
  uses-material-design: true
  
  fonts:
    - family: Phetsarath OT
      fonts:
        - asset: assets/fonts/Phetsarath_OT.ttf
```

### 5.3 Main App Entry Point

```dart
// lib/main.dart
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:supabase_flutter/supabase_flutter.dart';
import 'app.dart';
import 'config/constants.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  
  // Initialize Supabase
  await Supabase.initialize(
    url: Constants.supabaseUrl,
    anonKey: Constants.supabaseAnonKey,
  );
  
  // Initialize Hive for local storage
  await Hive.initFlutter();
  
  runApp(
    const ProviderScope(
      child: LaoKnowledgeHubApp(),
    ),
  );
}
```

```dart
// lib/config/constants.dart
class Constants {
  // Supabase - use environment variables in production
  static const String supabaseUrl = String.fromEnvironment(
    'SUPABASE_URL',
    defaultValue: 'https://your-project.supabase.co',
  );
  
  static const String supabaseAnonKey = String.fromEnvironment(
    'SUPABASE_ANON_KEY',
    defaultValue: 'your-anon-key',
  );
  
  // API Base URL (FastAPI on Firebase Cloud Run)
  static const String apiBaseUrl = String.fromEnvironment(
    'API_BASE_URL',
    defaultValue: 'https://your-api.run.app',
  );
  
  // Feature flags
  static const bool enableRentals = true;
  static const int maxDevicesPerUser = 3;
}
```

### 5.4 Supabase Service

```dart
// lib/core/services/supabase_service.dart
import 'package:supabase_flutter/supabase_flutter.dart';

class SupabaseService {
  final SupabaseClient _client;
  
  SupabaseService(this._client);
  
  // Auth
  Future<AuthResponse> signIn(String email, String password) {
    return _client.auth.signInWithPassword(
      email: email,
      password: password,
    );
  }
  
  Future<AuthResponse> signUp({
    required String email,
    required String password,
    required String fullName,
    String role = 'student',
  }) {
    return _client.auth.signUp(
      email: email,
      password: password,
      data: {
        'full_name': fullName,
        'role': role,
      },
    );
  }
  
  Future<void> signOut() => _client.auth.signOut();
  
  User? get currentUser => _client.auth.currentUser;
  Stream<AuthState> get authStateChanges => _client.auth.onAuthStateChange;
  
  // Books
  Future<List<Map<String, dynamic>>> getBooks({
    String? category,
    String? search,
    int page = 1,
    int limit = 20,
  }) async {
    var query = _client
        .from('books')
        .select('''
          *,
          profiles(full_name, avatar_url),
          book_categories(
            categories(name_la, name_en)
          )
        ''')
        .eq('status', 'published');
    
    if (category != null) {
      query = query.eq('book_categories.category_id', category);
    }
    
    if (search != null) {
      query = query.or('title_la.ilike.%$search%,title_en.ilike.%$search%');
    }
    
    final offset = (page - 1) * limit;
    query = query.range(offset, offset + limit - 1);
    
    final response = await query;
    return response;
  }
  
  Future<Map<String, dynamic>?> getBookById(String bookId) async {
    final response = await _client
        .from('books')
        .select('''
          *,
          profiles(full_name, avatar_url),
          chapters(*),
          book_categories(categories(*))
        ''')
        .eq('id', bookId)
        .single();
    
    return response;
  }
  
  // Get signed URL for reading
  Future<String> getBookReadUrl(String bookId) async {
    final response = await _client.rpc('get_book_read_url', params: {
      'p_book_id': bookId,
    });
    return response['signed_url'];
  }
  
  // Annotations
  Future<List<Map<String, dynamic>>> getAnnotations(String bookId) async {
    final response = await _client
        .from('annotations')
        .select('*')
        .eq('book_id', bookId)
        .eq('user_id', _client.auth.currentUser!.id);
    
    return response;
  }
  
  Future<Map<String, dynamic>> createAnnotation({
    required String bookId,
    required int pageNumber,
    required String type,
    String? content,
    String? color,
    Map<String, dynamic>? positionData,
  }) async {
    final response = await _client
        .from('annotations')
        .insert({
          'book_id': bookId,
          'user_id': _client.auth.currentUser!.id,
          'page_number': pageNumber,
          'annotation_type': type,
          'content': content,
          'color': color,
          'position_data': positionData,
        })
        .select()
        .single();
    
    return response;
  }
  
  // Storage
  Future<String> getCoverUrl(String path) async {
    return _client.storage.from('book-covers').getPublicUrl(path);
  }
}
```

### 5.5 Book Reader Screen (with Annotations)

```dart
// lib/features/reader/reader_screen.dart
import 'package:flutter/material.dart';
import 'package:syncfusion_flutter_pdfviewer/pdfviewer.dart';
import '../../core/services/supabase_service.dart';
import '../../models/annotation.dart';
import 'annotation_layer.dart';
import 'reader_toolbar.dart';

class ReaderScreen extends StatefulWidget {
  final String bookId;
  final String bookTitle;
  
  const ReaderScreen({
    super.key,
    required this.bookId,
    required this.bookTitle,
  });
  
  @override
  State<ReaderScreen> createState() => _ReaderScreenState();
}

class _ReaderScreenState extends State<ReaderScreen> {
  final GlobalKey<SfPdfViewerState> _viewerKey = GlobalKey();
  late Future<String> _pdfUrlFuture;
  List<Annotation> _annotations = [];
  bool _showToolbar = false;
  double _zoomLevel = 1.0;
  int _currentPage = 0;
  int _totalPages = 0;
  
  @override
  void initState() {
    super.initState();
    _loadBook();
  }
  
  Future<void> _loadBook() async {
    final supabase = SupabaseService(Supabase.instance.client);
    _pdfUrlFuture = supabase.getBookReadUrl(widget.bookId);
    _annotations = await supabase.getAnnotations(widget.bookId);
    setState(() {});
  }
  
  void _toggleToolbar() {
    setState(() => _showToolbar = !_showToolbar);
  }
  
  void _addAnnotation(Annotation annotation) async {
    final supabase = SupabaseService(Supabase.instance.client);
    await supabase.createAnnotation(
      bookId: widget.bookId,
      pageNumber: annotation.pageNumber,
      type: annotation.type,
      content: annotation.content,
      color: annotation.color,
      positionData: annotation.positionData,
    );
    setState(() => _annotations.add(annotation));
  }
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        children: [
          // PDF Viewer
          FutureBuilder<String>(
            future: _pdfUrlFuture,
            builder: (context, snapshot) {
              if (snapshot.connectionState == ConnectionState.waiting) {
                return const Center(child: CircularProgressIndicator());
              }
              
              if (snapshot.hasError) {
                return Center(
                  child: Text('Error loading book: ${snapshot.error}'),
                );
              }
              
              return SfPdfViewer.network(
                snapshot.data!,
                key: _viewerKey,
                onDocumentLoaded: (details) {
                  setState(() => _totalPages = details.pageCount);
                },
                onPageChanged: (details) {
                  setState(() => _currentPage = details.newPageNumber);
                },
                onTap: (_) => _toggleToolbar(),
                zoomLevel: _zoomLevel,
              );
            },
          ),
          
          // Toolbar (overlay)
          if (_showToolbar)
            ReaderToolbar(
              currentPage: _currentPage,
              totalPages: _totalPages,
              zoomLevel: _zoomLevel,
              onPageChanged: (page) {
                _viewerKey.currentState?.jumpToPage(page);
              },
              onZoomChanged: (zoom) {
                setState(() => _zoomLevel = zoom);
              },
              onAddAnnotation: (type) {
                // Add annotation mode
                _addAnnotation(Annotation(
                  type: type,
                  pageNumber: _currentPage,
                  color: 'yellow',
                ));
              },
              onClose: _toggleToolbar,
            ),
        ],
      ),
    );
  }
}
```

### 5.6 Book List Screen

```dart
// lib/features/books/book_list_screen.dart
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import '../../core/services/supabase_service.dart';
import 'book_card.dart';
import 'book_detail_screen.dart';

class BookListScreen extends ConsumerStatefulWidget {
  const BookListScreen({super.key});
  
  @override
  ConsumerState<BookListScreen> createState() => _BookListScreenState();
}

class _BookListScreenState extends ConsumerState<BookListScreen> {
  final _searchController = TextEditingController();
  String? _selectedCategory;
  int _currentPage = 1;
  bool _isLoading = false;
  List<Map<String, dynamic>> _books = [];
  
  @override
  void dispose() {
    _searchController.dispose();
    super.dispose();
  }
  
  Future<void> _loadBooks() async {
    if (_isLoading) return;
    setState(() => _isLoading = true);
    
    try {
      final supabase = SupabaseService(Supabase.instance.client);
      final books = await supabase.getBooks(
        category: _selectedCategory,
        search: _searchController.text,
        page: _currentPage,
        limit: 20,
      );
      
      setState(() {
        _books = _currentPage == 1 ? books : [..._books, ...books];
        _isLoading = false;
      });
    } catch (e) {
      setState(() => _isLoading = false);
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('Error loading books: $e')),
        );
      }
    }
  }
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Lao Knowledge Hub'),
        actions: [
          IconButton(
            icon: const Icon(Icons.shopping_cart),
            onPressed: () => context.push('/cart'),
          ),
          IconButton(
            icon: const Icon(Icons.person),
            onPressed: () => context.push('/profile'),
          ),
        ],
      ),
      body: Column(
        children: [
          // Search bar
          Padding(
            padding: const EdgeInsets.all(16),
            child: TextField(
              controller: _searchController,
              decoration: InputDecoration(
                hintText: 'Search books...',
                prefixIcon: const Icon(Icons.search),
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(12),
                ),
              ),
              onChanged: (_) => setState(() => _currentPage = 1),
            ),
          ),
          
          // Category chips
          SizedBox(
            height: 40,
            child: ListView(
              scrollDirection: Axis.horizontal,
              padding: const EdgeInsets.symmetric(horizontal: 16),
              children: [
                FilterChip(
                  label: const Text('All'),
                  selected: _selectedCategory == null,
                  onSelected: (_) {
                    setState(() {
                      _selectedCategory = null;
                      _currentPage = 1;
                    });
                    _loadBooks();
                  },
                ),
                // Add more category chips from API
              ],
            ),
          ),
          const SizedBox(height: 16),
          
          // Book grid
          Expanded(
            child: GridView.builder(
              padding: const EdgeInsets.all(16),
              gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                crossAxisCount: 2,
                childAspectRatio: 0.7,
                crossAxisSpacing: 16,
                mainAxisSpacing: 16,
              ),
              itemCount: _books.length + (_isLoading ? 1 : 0),
              itemBuilder: (context, index) {
                if (index == _books.length) {
                  return const Center(child: CircularProgressIndicator());
                }
                
                final book = _books[index];
                return BookCard(
                  book: book,
                  onTap: () => context.push('/books/${book['id']}'),
                );
              },
            ),
          ),
        ],
      ),
    );
  }
}
```

---

## 6. Next.js SEO Layer (Public Web)

### 6.1 Purpose

The Next.js layer serves **public-facing pages** that need to be indexed by search engines:
- Book catalog (`/books`)
- Book detail pages (`/books/[id]`)
- Author profiles (`/authors/[id]`)
- Landing pages

Authenticated user actions (reading, cart, library) are handled by **Flutter Web**.

### 6.2 Project Structure

```
nextjs-seo/
├── src/
│   ├── app/
│   │   ├── books/
│   │   │   ├── page.tsx          # Book catalog
│   │   │   └── [id]/
│   │   │       └── page.tsx      # Book detail
│   │   ├── authors/
│   │   │   └── [id]/page.tsx     # Author profile
│   │   ├── layout.tsx
│   │   └── page.tsx              # Homepage
│   ├── components/
│   │   ├── BookCard.tsx
│   │   ├── BookList.tsx
│   │   └── SeoHead.tsx
│   ├── lib/
│   │   ├── supabase.ts           # Supabase client
│   │   └── api.ts                # API calls
│   └── styles/
│       └── globals.css
├── next.config.js
└── package.json
```

### 6.3 Book Detail Page (with SEO)

```typescript
// src/app/books/[id]/page.tsx
import { Metadata } from 'next';
import { supabase } from '@/lib/supabase';
import { SeoHead } from '@/components/SeoHead';
import { BookDetail } from '@/components/BookDetail';

interface PageProps {
  params: { id: string };
}

export async function generateMetadata({ params }: PageProps): Promise<Metadata> {
  const book = await supabase
    .from('books')
    .select('*, profiles(full_name)')
    .eq('id', params.id)
    .single();

  if (!book) {
    return { title: 'Book Not Found' };
  }

  return {
    title: `${book.data.title_la} | Lao Knowledge Hub`,
    description: book.data.description_la,
    openGraph: {
      title: book.data.title_la,
      description: book.data.description_la,
      images: [book.data.cover_image_url],
      authors: [book.data.profiles.full_name],
    },
  };
}

export default async function BookPage({ params }: PageProps) {
  const book = await supabase
    .from('books')
    .select('*, profiles(*), chapters(*)')
    .eq('id', params.id)
    .single();

  if (!book) {
    return <div>Book not found</div>;
  }

  return (
    <>
      <SeoHead book={book.data} />
      <BookDetail book={book.data} />
      <a
        href="https://your-project.web.app/books/${params.id}/read"
        className="btn-primary"
      >
        Read Now (Open App)
      </a>
    </>
  );
}
```

### 6.4 Deployment to Firebase Hosting

```bash
# Install Firebase CLI
npm install -g firebase-tools

# Initialize Firebase
firebase init hosting

# Select:
# - Public directory: out (for static export)
# - Single-page app: No
# - GitHub integration: Optional

# Build for production
npm run build  # Creates 'out' directory

# Deploy
firebase deploy --only hosting
```

```javascript
// next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',  // Static export for Firebase Hosting
  images: {
    unoptimized: true,  // Required for static export
  },
};

module.exports = nextConfig;
```

---

## 7. Deployment & DevOps

### 7.1 Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    Firebase Hosting                             │
│  ┌─────────────────────┐  ┌─────────────────────────────────┐  │
│  │   Flutter Web App   │  │    Next.js SEO Site (Static)    │  │
│  │   (your-project.    │  │    (your-project.web.app)       │  │
│  │    web.app)         │  │                                 │  │
│  └─────────────────────┘  └─────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│              Firebase Cloud Run (FastAPI Backend)               │
│         API: payments, DRM, complex business logic              │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     Supabase (Managed)                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐  │
│  │  PostgreSQL  │  │     Auth     │  │      Storage         │  │
│  │  (Database)  │  │  (JWT/OAuth) │  │  (PDFs, Covers)      │  │
│  └──────────────┘  └──────────────┘  └──────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                  React Admin (Separate Deploy)                  │
│         Admin dashboard for content moderation                  │
└─────────────────────────────────────────────────────────────────┘
```

### 7.2 Environment Configuration

```bash
# .env.example (Backend - FastAPI)
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_SERVICE_KEY=your-service-role-key
SUPABASE_ANON_KEY=your-anon-key

BCEL_MERCHANT_ID=xxx
BCEL_SECRET_KEY=xxx

API_BASE_URL=https://your-api.run.app
FRONTEND_URL=https://your-project.web.app

# .env.example (Flutter)
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_ANON_KEY=your-anon-key
API_BASE_URL=https://your-api.run.app

# .env.example (Next.js)
NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key
```

### 7.3 Deploy FastAPI to Cloud Run

```dockerfile
# Dockerfile (backend)
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
```

```bash
# Deploy to Cloud Run
gcloud run deploy lao-knowledge-hub-api \
  --source ./backend \
  --platform managed \
  --region asia-southeast1 \
  --allow-unauthenticated \
  --set-env-vars SUPABASE_URL=xxx,SUPABASE_SERVICE_KEY=xxx
```

### 7.4 Deploy Flutter Web to Firebase

```bash
# Build Flutter Web
flutter build web --release --base-href="/app/"

# Deploy to Firebase Hosting
firebase deploy --only hosting:flutter
```

```json
// firebase.json
{
  "hosting": [
    {
      "target": "flutter",
      "public": "build/web",
      "rewrites": [
        {
          "source": "**",
          "destination": "/index.html"
        }
      ]
    },
    {
      "target": "nextjs",
      "public": "nextjs-seo/out",
      "rewrites": []
    }
  ]
}
```

### 7.5 Deploy React Admin

```bash
# Create React Admin app
npx create-react-app admin-dashboard
cd admin-dashboard
npm install react-admin ra-data-supabase

# Deploy to separate Firebase target
firebase deploy --only hosting:admin
```

```typescript
// src/dataProvider.ts
import { supabaseDataProvider } from 'ra-data-supabase';
import { createClient } from '@supabase/supabase-js';

const supabase = createClient(
  process.env.REACT_APP_SUPABASE_URL!,
  process.env.REACT_APP_SUPABASE_SERVICE_KEY!
);

export const dataProvider = supabaseDataProvider({
  supabaseClient: supabase,
  supabaseApiUrl: process.env.REACT_APP_SUPABASE_URL,
});
```

### 7.6 CI/CD Pipeline (GitHub Actions)

```yaml
# .github/workflows/deploy.yml
name: Deploy

on:
  push:
    branches: [main]

jobs:
  deploy-backend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: google-github-actions/deploy-cloudrun@v2
        with:
          service: lao-knowledge-hub-api
          region: asia-southeast1
          source: ./backend

  deploy-frontend:
    runs-on: ubuntu-latest
    needs: deploy-backend
    steps:
      - uses: actions/checkout@v4
      - uses: subosito/flutter-action@v2
        with:
          flutter-version: '3.19.0'
      - run: flutter build web --release
      - uses: FirebaseExtended/action-hosting-deploy@v0
        with:
          repoToken: '${{ secrets.GITHUB_TOKEN }}'
          firebaseServiceAccount: '${{ secrets.FIREBASE_SERVICE_ACCOUNT }}'
          channelId: live
          projectId: your-project-id

  deploy-seo:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: cd nextjs-seo && npm ci && npm run build
      - uses: FirebaseExtended/action-hosting-deploy@v0
        with:
          repoToken: '${{ secrets.GITHUB_TOKEN }}'
          firebaseServiceAccount: '${{ secrets.FIREBASE_SERVICE_ACCOUNT }}'
          channelId: live
          projectId: your-project-id
```

---

## 8. Development Phases & Timeline

### Phase 1: Foundation (Weeks 1-4)

| Week | Tasks | Deliverables |
|------|-------|--------------|
| 1 | Supabase setup, database schema, RLS policies | Working auth, DB ready |
| 2 | FastAPI setup, book CRUD endpoints | Book management API |
| 3 | Flutter app setup, book listing UI | Browseable catalog (Flutter) |
| 4 | Book detail screen, Supabase Storage | Book pages with cover upload |

**Milestone 1:** Professors can upload books, users can browse and preview

### Phase 2: Commerce (Weeks 5-8)

| Week | Tasks | Deliverables |
|------|-------|--------------|
| 5 | Cart system (Flutter), order creation | Shopping cart |
| 6 | BCEL One integration (FastAPI) | Payment processing |
| 7 | Purchase verification, access granting | Post-purchase flow |
| 8 | User library screen, reading history | "My Books" section |

**Milestone 2:** End-to-end purchase flow working

### Phase 3: Reader & Annotations (Weeks 9-12)

| Week | Tasks | Deliverables |
|------|-------|--------------|
| 9 | Syncfusion PDF viewer integration | Basic PDF reader |
| 10 | Annotation system (highlights, notes) | Study tools |
| 11 | Signed URLs, DRM implementation | Content protection |
| 12 | Device limiting, testing | Security features |

**Milestone 3:** Full reading experience with annotations

### Phase 4: SEO Layer & Admin (Weeks 13-16)

| Week | Tasks | Deliverables |
|------|-------|--------------|
| 13 | Next.js setup, book catalog pages | SEO-friendly listing |
| 14 | React Admin dashboard | Content moderation UI |
| 15 | Royalty tracking, statements | Author payment system |
| 16 | Testing, bug fixes, polish | Production-ready |

**Milestone 4:** Production-ready platform with SEO

### Phase 5: Launch Prep (Weeks 17-20)

| Week | Tasks | Deliverables |
|------|-------|--------------|
| 17 | Performance optimization | Fast load times |
| 18 | Security audit, BCEL testing | Security report |
| 19 | Content onboarding (professors) | Initial book catalog |
| 20 | Soft launch with NUOL partners | Live pilot |

**Milestone 5:** Public launch ready

---

## 9. Testing Strategy

### 9.1 Unit Tests (Flutter)

```dart
// test/services/supabase_service_test.dart
import 'package:flutter_test/flutter_test.dart';

void main() {
  group('SupabaseService', () {
    test('getBooks returns list of books', () async {
      // Mock Supabase client
      // Test book listing logic
    });

    test('createAnnotation saves annotation', () async {
      // Test annotation creation
    });
  });
}
```

### 9.2 API Tests (FastAPI)

```python
# tests/test_books.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_list_books():
    response = client.get("/api/books")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_book_requires_auth():
    response = client.post("/api/books", json={})
    assert response.status_code == 401
```

### 9.3 E2E Tests (Flutter Integration Test)

```dart
// integration_test/purchase_flow_test.dart
import 'package:flutter_test/flutter_test.dart';
import 'package:integration_test/integration_test.dart';

void main() {
  IntegrationTestWidgetsFlutterBinding.ensureInitialized();

  testWidgets('Complete purchase flow', (tester) async {
    await tester.pumpWidget(MyApp());
    await tester.pumpAndSettle();

    // Tap on a book
    await tester.tap(find.text('Book Title'));
    await tester.pumpAndSettle();

    // Add to cart
    await tester.tap(find.text('Add to Cart'));
    await tester.pumpAndSettle();

    // Navigate to checkout
    await tester.tap(find.text('Checkout'));
    await tester.pumpAndSettle();
  });
}
```

---

## 10. Risk Mitigation

| Risk | Impact | Mitigation |
|------|--------|------------|
| BCEL API delays/unreliable | High | Implement manual bank transfer fallback; reconcile manually |
| PDF piracy (screenshots, sharing) | High | Social DRM (watermarking) + convenient pricing + legal terms |
| Low professor adoption | High | Offer digitization service; advance royalty payments |
| Flutter Web performance | Medium | Optimize build; lazy loading; CDN via Firebase |
| Lao font rendering on Web | Medium | Bundle Phetsarath OT; test on all browsers |
| Supabase rate limits | Medium | Implement caching; optimize queries; upgrade plan if needed |
| Cloud Run cold starts | Medium | Keep minimum 1 instance; use Cloud Run requests-based scaling |

---

## 11. Success Metrics

### Launch Criteria (MVP)
- [ ] 20+ books from 10+ professors
- [ ] End-to-end purchase flow working (BCEL + fallback)
- [ ] Reader with annotations functional (Flutter)
- [ ] SEO pages indexed by Google (Next.js)
- [ ] 100+ registered users (beta testers)

### Post-Launch KPIs
| Metric | Target (3 months) | Target (12 months) |
|--------|-------------------|--------------------|
| Monthly Active Users | 500 | 5,000 |
| Books Available | 50 | 500 |
| Conversion Rate | 3% | 5% |
| Average Order Value | 50,000 LAK | 75,000 LAK |
| User Retention (30-day) | 40% | 60% |
| SEO Organic Traffic | 1,000/month | 10,000/month |

---

## 12. Next Steps

1. **Review and approve** this implementation plan
2. **Set up development environment:**
   - Create Supabase project
   - Set up Firebase project
   - Create Google Cloud project (for Cloud Run)
   - Initialize GitHub repositories
3. **Begin Phase 1** development (Supabase + FastAPI + Flutter)
4. **Parallel track:** Initiate BCEL partnership discussions
5. **Parallel track:** Begin professor outreach for content onboarding
6. **Parallel track:** Start NUOL partnership formalization

---

## Appendix: Technology Summary

| Component | Technology | Why |
|-----------|------------|-----|
| **Mobile + Web App** | Flutter | Single codebase, reduces dev time 50%+ |
| **SEO Layer** | Next.js | Server-side rendering for Google indexing |
| **Backend API** | FastAPI (Python) | Team comfort, fast development |
| **Database + Auth** | Supabase | PostgreSQL + Auth + Storage + RLS out-of-box |
| **File Storage** | Supabase Storage | Integrated, signed URLs for DRM |
| **PDF Viewer** | Syncfusion (Flutter) | Native annotations, good performance |
| **Admin Dashboard** | React Admin + Supabase | Rapid admin panel development |
| **Hosting (Frontend)** | Firebase Hosting | Free SSL, CDN, easy deployment |
| **Hosting (Backend)** | Cloud Run | Serverless, auto-scaling, Python-friendly |
| **Payments** | BCEL One API | Local payment standard |

---

*Document Version: 1.1 | Updated: 2026-02-24 | Stack: Flutter + FastAPI + Supabase + Firebase*
