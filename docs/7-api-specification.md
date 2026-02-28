# Lao Knowledge Hub - API Specification

**Version:** 1.0  
**Date:** 2026-02-25  
**Framework:** FastAPI  
**Base URL:** `https://api.laoknowledgehub.la/api/v1`

---

## Overview

This document specifies all API endpoints for the Lao Knowledge Hub platform. The API follows RESTful conventions and uses JWT authentication via Supabase.

---

## Authentication

All authenticated endpoints require a Bearer token obtained from Supabase Auth.

```http
Authorization: Bearer <supabase_jwt_token>
```

### Authentication Flow

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   Client     │────▶│   Supabase   │────▶│   FastAPI    │
│  (Flutter)   │     │     Auth     │     │   Backend    │
└──────────────┘     └──────────────┘     └──────────────┘
       │                    │                    │
       │  1. Login          │                    │
       │───────────────────▶│                    │
       │                    │                    │
       │  2. Return JWT     │                    │
       │◀───────────────────│                    │
       │                    │                    │
       │  3. Request with JWT                    │
       │────────────────────────────────────────▶│
       │                    │                    │
       │                    │  4. Verify JWT     │
       │                    │───────────────────▶│
       │                    │                    │
       │  5. Response       │                    │
       │◀────────────────────────────────────────│
       │                    │                    │
```

---

## API Endpoints

### Health Check

#### `GET /health`

Check API health status.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2026-02-25T10:30:00Z",
  "version": "1.0.0"
}
```

---

## Authentication Endpoints

### `POST /auth/me`

Get current user profile.

**Headers:**
```
Authorization: Bearer <token>
```

**Response:** `200 OK`
```json
{
  "id": "uuid",
  "email": "user@example.com",
  "full_name": "ສົມສັກ ລາວວົງສີ",
  "phone": "+856 20 1234 5678",
  "role": "student",
  "avatar_url": "https://...",
  "university": {
    "id": "uuid",
    "name_la": "ມະຫາວິທະຍາໄລແຫ່ງຊາດລາວ",
    "name_en": "National University of Laos",
    "code": "NUOL"
  },
  "faculty": {
    "id": "uuid",
    "name_la": "ຄະນະເສດຖະສາດ",
    "name_en": "Faculty of Economics"
  },
  "is_verified": true,
  "created_at": "2026-01-01T00:00:00Z"
}
```

---

### `POST /auth/devices/register`

Register device for DRM (max 3 devices per user).

**Headers:**
```
Authorization: Bearer <token>
Content-Type: application/json
```

**Request:**
```json
{
  "device_fingerprint": "unique-device-id-xyz",
  "device_name": "iPhone 13",
  "device_type": "mobile"
}
```

**Response:** `201 Created`
```json
{
  "id": "uuid",
  "device_name": "iPhone 13",
  "device_type": "mobile",
  "registered_at": "2026-02-25T10:30:00Z",
  "is_active": true
}
```

**Errors:**
- `403 Forbidden` - Device limit reached (max 3)

---

### `GET /auth/devices`

List registered devices.

**Response:** `200 OK`
```json
[
  {
    "id": "uuid",
    "device_name": "iPhone 13",
    "device_type": "mobile",
    "last_active_at": "2026-02-25T10:30:00Z"
  },
  {
    "id": "uuid",
    "device_name": "iPad Pro",
    "device_type": "tablet",
    "last_active_at": "2026-02-24T15:20:00Z"
  }
]
```

---

### `DELETE /auth/devices/{device_id}`

Remove a registered device.

**Response:** `204 No Content`

---

## Books Endpoints

### `GET /books`

List published books with filters and pagination.

**Query Parameters:**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `page` | integer | 1 | Page number |
| `limit` | integer | 20 | Items per page (max 100) |
| `category` | string | - | Category slug |
| `search` | string | - | Search query (title, description) |
| `university` | string | - | University code |
| `faculty` | string | - | Faculty code |
| `sort` | string | `published_at` | Sort field |
| `order` | string | `desc` | Sort order (`asc`, `desc`) |

**Example:**
```
GET /books?page=1&limit=20&category=sciences&search=ບັນຊີ
```

**Response:** `200 OK`
```json
{
  "data": [
    {
      "id": "uuid",
      "title_la": "ພື້ນຖານການບັນຊີ",
      "title_en": "Fundamentals of Accounting",
      "author": {
        "id": "uuid",
        "full_name": "ຮສ. ດຣ. ສົມສັກ ລາວວົງສີ",
        "avatar_url": "https://..."
      },
      "cover_image_url": "https://...",
      "price_lak": 50000,
      "rental_price_lak": 25000,
      "rating": 4.8,
      "review_count": 23,
      "purchase_count": 156,
      "categories": [
        {
          "slug": "economics",
          "name_la": "ເສດຖະສາດ",
          "name_en": "Economics"
        }
      ],
      "is_featured": true,
      "published_at": "2026-01-15T00:00:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 150,
    "total_pages": 8
  }
}
```

---

### `GET /books/{id}`

Get book details.

**Response:** `200 OK`
```json
{
  "id": "uuid",
  "title_la": "ພື້ນຖານການບັນຊີ",
  "title_en": "Fundamentals of Accounting",
  "description_la": "...",
  "description_en": "...",
  "author": {
    "id": "uuid",
    "full_name": "ຮສ. ດຣ. ສົມສັກ ລາວວົງສີ",
    "title": "Associate Professor",
    "faculty": "Faculty of Economics, NUOL",
    "avatar_url": "https://...",
    "bio_la": "...",
    "bio_en": "..."
  },
  "cover_image_url": "https://...",
  "file_size": 15728640,
  "page_count": 250,
  "isbn": "978-99919-0-123-4",
  "price_lak": 50000,
  "rental_price_lak": 25000,
  "rental_period_days": 120,
  "royalty_percentage": 70.0,
  "rating": 4.8,
  "review_count": 23,
  "view_count": 1234,
  "purchase_count": 156,
  "categories": [...],
  "chapters": [
    {
      "id": "uuid",
      "title_la": "ບົດທີ 1: ບົດນຳ",
      "title_en": "Chapter 1: Introduction",
      "page_start": 1,
      "page_end": 15,
      "sort_order": 1
    }
  ],
  "courses": [
    {
      "id": "uuid",
      "code": "ACC101",
      "name_la": "ບົດນຳການບັນຊີ",
      "relationship_type": "required"
    }
  ],
  "published_at": "2026-01-15T00:00:00Z",
  "created_at": "2026-01-01T00:00:00Z"
}
```

**Errors:**
- `404 Not Found` - Book not found or not published

---

### `GET /books/{id}/sample`

Get signed URL for sample pages (first 10 pages or configured sample_pages).

**Response:** `200 OK`
```json
{
  "signed_url": "https://...?X-Amz-Algorithm=...&X-Amz-Expires=3600",
  "expires_at": "2026-02-25T11:30:00Z",
  "sample_pages": 10
}
```

**Note:** URL expires in 1 hour.

---

### `GET /books/{id}/read`

Get signed URL for full book (if purchased or rented).

**Headers:**
```
Authorization: Bearer <token>
```

**Response:** `200 OK`
```json
{
  "signed_url": "https://...?X-Amz-Algorithm=...",
  "expires_at": "2026-02-25T12:30:00Z",
  "access_type": "purchase",
  "expires_on": null
}
```

**Errors:**
- `403 Forbidden` - Book not purchased
- `403 Forbidden` - Rental expired

---

### `POST /books`

Create a new book (professors only).

**Headers:**
```
Authorization: Bearer <token>
Content-Type: application/json
```

**Request:**
```json
{
  "title_la": "ພື້ນຖານການບັນຊີ",
  "title_en": "Fundamentals of Accounting",
  "description_la": "...",
  "description_en": "...",
  "price_lak": 50000,
  "rental_price_lak": 25000,
  "royalty_percentage": 70.0,
  "category_ids": ["uuid1", "uuid2"],
  "chapter_titles": [
    "ບົດທີ 1: ບົດນຳ",
    "ບົດທີ 2: ສົມຜົນການບັນຊີ"
  ]
}
```

**Response:** `201 Created`
```json
{
  "id": "uuid",
  "title_la": "ພື້ນຖານການບັນຊີ",
  "status": "pending_review",
  "created_at": "2026-02-25T10:30:00Z"
}
```

**Errors:**
- `403 Forbidden` - User is not a professor

---

### `PUT /books/{id}`

Update book (author only).

**Request:** (same as POST, all fields optional)

**Response:** `200 OK`

**Errors:**
- `403 Forbidden` - Not the author
- `400 Bad Request` - Cannot update published book

---

### `DELETE /books/{id}`

Delete book (author only, draft status only).

**Response:** `204 No Content`

**Errors:**
- `403 Forbidden` - Not the author
- `400 Bad Request` - Cannot delete published book

---

### `GET /books/{id}/stats`

Get book statistics (author only).

**Response:** `200 OK`
```json
{
  "view_count": 1234,
  "purchase_count": 156,
  "rental_count": 89,
  "revenue_lak": 7800000,
  "royalty_earned_lak": 5460000,
  "rating_average": 4.8,
  "review_count": 23,
  "daily_views": [
    {"date": "2026-02-24", "count": 45},
    {"date": "2026-02-25", "count": 52}
  ]
}
```

---

## Categories Endpoints

### `GET /categories`

List all categories.

**Response:** `200 OK`
```json
[
  {
    "id": "uuid",
    "name_la": "ເສດຖະສາດ",
    "name_en": "Economics",
    "slug": "economics",
    "parent_id": null,
    "book_count": 45,
    "icon_url": "https://..."
  }
]
```

---

## Universities & Faculties

### `GET /universities`

List all universities.

**Response:** `200 OK`
```json
[
  {
    "id": "uuid",
    "name_la": "ມະຫາວິທະຍາໄລແຫ່ງຊາດລາວ",
    "name_en": "National University of Laos",
    "code": "NUOL",
    "logo_url": "https://...",
    "faculty_count": 12
  }
]
```

---

### `GET /universities/{id}/faculties`

List faculties for a university.

**Response:** `200 OK`
```json
[
  {
    "id": "uuid",
    "name_la": "ຄະນະເສດຖະສາດ",
    "name_en": "Faculty of Economics",
    "code": "ECO",
    "dean": {
      "full_name": "..."
    },
    "book_count": 34
  }
]
```

---

## Courses Endpoints

### `GET /courses`

List courses with filters.

**Query Parameters:**
- `university_id` - Filter by university
- `faculty_id` - Filter by faculty
- `search` - Search by code or name

**Response:** `200 OK`
```json
[
  {
    "id": "uuid",
    "code": "ACC101",
    "name_la": "ບົດນຳການບັນຊີ",
    "name_en": "Introduction to Accounting",
    "semester": "1",
    "year": 1,
    "credits": 3,
    "required_books": [
      {
        "id": "uuid",
        "title_la": "ພື້ນຖານການບັນຊີ"
      }
    ]
  }
]
```

---

## Orders & Checkout

### `POST /cart/checkout`

Create order and initiate payment.

**Headers:**
```
Authorization: Bearer <token>
Content-Type: application/json
```

**Request:**
```json
{
  "items": [
    {
      "book_id": "uuid",
      "purchase_type": "purchase"
    },
    {
      "book_id": "uuid",
      "purchase_type": "rental"
    }
  ],
  "payment_method": "bcel_one",
  "return_url": "https://laoknowledgehub.la/payment/return"
}
```

**Response:** `201 Created`
```json
{
  "order_id": "uuid",
  "order_number": "ORD-20260225-000001",
  "total_amount": 75000,
  "payment_url": "https://bcel.com.kh/payment?...",
  "expires_at": "2026-02-25T11:00:00Z"
}
```

**Errors:**
- `400 Bad Request` - Cart is empty
- `400 Bad Request` - Book already owned

---

### `GET /orders`

List user orders.

**Response:** `200 OK`
```json
[
  {
    "id": "uuid",
    "order_number": "ORD-20260225-000001",
    "total_amount": 75000,
    "payment_status": "completed",
    "payment_method": "bcel_one",
    "items_count": 2,
    "created_at": "2026-02-25T10:30:00Z"
  }
]
```

---

### `GET /orders/{id}`

Get order details.

**Response:** `200 OK`
```json
{
  "id": "uuid",
  "order_number": "ORD-20260225-000001",
  "total_amount": 75000,
  "discount_amount": 0,
  "final_amount": 75000,
  "payment_status": "completed",
  "payment_method": "bcel_one",
  "bcel_transaction_id": "BCEL123456",
  "items": [
    {
      "id": "uuid",
      "book": {
        "id": "uuid",
        "title_la": "ພື້ນຖານການບັນຊີ",
        "cover_image_url": "https://..."
      },
      "price_at_purchase": 50000,
      "royalty_amount": 35000,
      "purchase_type": "purchase",
      "access_expires_at": null
    },
    {
      "id": "uuid",
      "book": {
        "id": "uuid",
        "title_la": "ເສດຖະສາດຈຸລະພາກ",
        "cover_image_url": "https://..."
      },
      "price_at_purchase": 25000,
      "royalty_amount": 17500,
      "purchase_type": "rental",
      "rental_end_date": "2026-06-25",
      "access_expires_at": "2026-06-25T23:59:59Z"
    }
  ],
  "created_at": "2026-02-25T10:30:00Z"
}
```

---

### `POST /orders/{id}/refund`

Request refund for an order.

**Request:**
```json
{
  "reason": "Wrong book purchased"
}
```

**Response:** `200 OK`
```json
{
  "refund_request_id": "uuid",
  "status": "pending_review",
  "message": "Refund request submitted. We will review within 3-5 business days."
}
```

**Errors:**
- `400 Bad Request` - Order too old for refund (7 days max)

---

## Payments

### `POST /payments/bcel/initiate`

Initiate BCEL One payment.

**Request:**
```json
{
  "order_id": "uuid",
  "amount": 75000,
  "return_url": "https://...",
  "cancel_url": "https://..."
}
```

**Response:** `200 OK`
```json
{
  "payment_url": "https://bcel.com.kh/payment?...",
  "transaction_id": "BCEL123456"
}
```

---

### `POST /payments/bcel/callback`

BCEL payment callback (server-to-server).

**Request:** (from BCEL)
```json
{
  "transaction_id": "BCEL123456",
  "order_id": "uuid",
  "status": "success",
  "amount": 75000,
  "signature": "hmac_signature"
}
```

**Response:** `200 OK`
```json
{
  "status": "received"
}
```

---

## Annotations

### `GET /books/{id}/annotations`

Get user annotations for a book.

**Query Parameters:**
- `type` - Filter by type (highlight, note, bookmark)
- `color` - Filter by color
- `page` - Filter by page number

**Response:** `200 OK`
```json
[
  {
    "id": "uuid",
    "book_id": "uuid",
    "page_number": 45,
    "annotation_type": "highlight",
    "content": "Double-entry ensures the accounting equation remains balanced.",
    "color": "yellow",
    "position_data": {
      "x": 100,
      "y": 200,
      "width": 300,
      "height": 20
    },
    "tags": ["important", "exam"],
    "created_at": "2026-02-25T10:30:00Z",
    "updated_at": "2026-02-25T10:30:00Z"
  }
]
```

---

### `POST /annotations`

Create annotation.

**Request:**
```json
{
  "book_id": "uuid",
  "page_number": 45,
  "annotation_type": "highlight",
  "content": "Important concept",
  "color": "yellow",
  "position_data": {...},
  "tags": ["important"]
}
```

**Response:** `201 Created`

---

### `PUT /annotations/{id}`

Update annotation.

**Request:** (all fields optional)

**Response:** `200 OK`

---

### `DELETE /annotations/{id}`

Delete annotation.

**Response:** `204 No Content`

---

### `POST /annotations/export`

Export annotations to Word/PDF.

**Request:**
```json
{
  "book_id": "uuid",
  "format": "docx",
  "include_highlights": true,
  "include_notes": true,
  "group_by": "chapter"
}
```

**Response:** `200 OK`
```json
{
  "export_url": "https://.../exports/annotations-123.docx",
  "expires_at": "2026-02-25T12:30:00Z"
}
```

---

## Reading Progress

### `GET /books/{id}/progress`

Get reading progress for a book.

**Response:** `200 OK`
```json
{
  "book_id": "uuid",
  "last_page": 45,
  "progress_percentage": 18.0,
  "last_read_at": "2026-02-25T10:30:00Z",
  "total_time_minutes": 120,
  "sessions_count": 5
}
```

---

### `POST /progress/sync`

Sync reading progress.

**Request:**
```json
{
  "book_id": "uuid",
  "last_page": 45,
  "progress_percentage": 18.0,
  "time_read_minutes": 25,
  "session_id": "uuid"
}
```

**Response:** `200 OK`
```json
{
  "synced": true,
  "last_page": 45,
  "progress_percentage": 18.0
}
```

---

### `GET /progress/start-session`

Start a study session.

**Request:**
```json
{
  "book_id": "uuid"
}
```

**Response:** `200 OK`
```json
{
  "session_id": "uuid",
  "started_at": "2026-02-25T10:30:00Z"
}
```

---

### `POST /progress/end-session`

End a study session.

**Request:**
```json
{
  "session_id": "uuid",
  "pages_read": 10,
  "annotations_created": 3
}
```

**Response:** `200 OK`
```json
{
  "session_id": "uuid",
  "ended_at": "2026-02-25T11:30:00Z",
  "duration_minutes": 60,
  "pages_read": 10
}
```

---

## Reviews

### `GET /books/{id}/reviews`

Get reviews for a book.

**Query Parameters:**
- `page` - Page number
- `limit` - Items per page
- `sort` - Sort by (`recent`, `helpful`, `rating_high`, `rating_low`)

**Response:** `200 OK`
```json
{
  "data": [
    {
      "id": "uuid",
      "user": {
        "full_name": "ສົມສັກ ວົງສະຫວັດ",
        "avatar_url": "https://...",
        "is_verified_purchase": true
      },
      "rating": 5,
      "title": "ປຶ້ມດີຫຼາຍ",
      "content": "ອ່ານແລ້ວເຂົ້າໃຈງ່າຍ...",
      "helpful_count": 12,
      "created_at": "2026-02-20T00:00:00Z"
    }
  ],
  "pagination": {...},
  "summary": {
    "average_rating": 4.8,
    "total_reviews": 23,
    "rating_distribution": {
      "5": 18,
      "4": 4,
      "3": 1,
      "2": 0,
      "1": 0
    }
  }
}
```

---

### `POST /books/{id}/reviews`

Write a review.

**Request:**
```json
{
  "rating": 5,
  "title": "ປຶ້ມດີຫຼາຍ",
  "content": "ອ່ານແລ້ວເຂົ້າໃຈງ່າຍ..."
}
```

**Response:** `201 Created`

**Errors:**
- `400 Bad Request` - User hasn't purchased the book
- `400 Bad Request` - User already reviewed

---

### `POST /reviews/{id}/vote`

Vote on review helpfulness.

**Request:**
```json
{
  "is_helpful": true
}
```

**Response:** `200 OK`
```json
{
  "helpful_count": 13,
  "user_voted": true
}
```

---

## Royalties (Authors Only)

### `GET /royalties/statement`

Get royalty statements.

**Response:** `200 OK`
```json
[
  {
    "id": "uuid",
    "period_start": "2026-01-01",
    "period_end": "2026-01-31",
    "total_sales": 500000,
    "platform_fee": 150000,
    "total_royalty": 350000,
    "status": "paid",
    "paid_at": "2026-02-05T00:00:00Z",
    "payment_reference": "BANK123456"
  }
]
```

---

### `GET /royalties/statement/{id}`

Get detailed royalty statement.

**Response:** `200 OK`
```json
{
  "id": "uuid",
  "period_start": "2026-01-01",
  "period_end": "2026-01-31",
  "total_sales": 500000,
  "platform_fee": 150000,
  "total_royalty": 350000,
  "status": "paid",
  "line_items": [
    {
      "book": {
        "title_la": "ພື້ນຖານການບັນຊີ"
      },
      "sales_count": 10,
      "sale_amount": 500000,
      "royalty_percentage": 70.0,
      "royalty_amount": 350000
    }
  ]
}
```

---

## Admin Endpoints

### `GET /admin/books`

List all books (including drafts, pending).

**Query Parameters:**
- `status` - Filter by status

**Response:** `200 OK`

---

### `PUT /admin/books/{id}/review`

Review/approve book.

**Request:**
```json
{
  "status": "published",
  "rejection_reason": null
}
```

**Response:** `200 OK`

---

### `GET /admin/users`

List users.

**Response:** `200 OK`

---

### `GET /admin/analytics`

Get platform analytics.

**Response:** `200 OK`
```json
{
  "total_users": 1500,
  "total_books": 250,
  "total_orders": 3200,
  "total_revenue_lak": 160000000,
  "active_users_30d": 800,
  "top_categories": [...],
  "top_books": [...]
}
```

---

## Error Responses

### Standard Error Format

```json
{
  "error": {
    "code": "BOOK_NOT_FOUND",
    "message": "The requested book was not found or is not published.",
    "details": {
      "book_id": "uuid"
    }
  }
}
```

### Common Error Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `UNAUTHORIZED` | 401 | Missing or invalid token |
| `FORBIDDEN` | 403 | User lacks permission |
| `BOOK_NOT_FOUND` | 404 | Book doesn't exist |
| `ORDER_NOT_FOUND` | 404 | Order doesn't exist |
| `ALREADY_OWNED` | 400 | User already purchased book |
| `RENTAL_EXPIRED` | 403 | Rental access expired |
| `DEVICE_LIMIT_REACHED` | 403 | Max 3 devices reached |
| `VALIDATION_ERROR` | 400 | Invalid request data |
| `PAYMENT_FAILED` | 400 | Payment processing failed |

---

## Rate Limiting

| Endpoint Type | Limit |
|---------------|-------|
| Public (GET) | 100 requests/minute |
| Authenticated (GET) | 200 requests/minute |
| Write (POST/PUT/DELETE) | 50 requests/minute |
| File Downloads | 20 requests/minute |

**Headers:**
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1645776600
```

---

## Versioning

API version is included in the URL path:
```
/api/v1/books
/api/v1/orders
```

Backward compatibility is maintained for at least 2 versions.

---

## CORS

Allowed origins:
- `https://laoknowledgehub.la`
- `https://www.laoknowledgehub.la`
- `https://*.firebaseapp.com` (development)

---

## Next Steps

1. **Implement endpoints** - Start with P0 (books, auth, orders)
2. **Generate OpenAPI spec** - FastAPI auto-generates at `/docs`
3. **Create API client** - Flutter HTTP wrapper
4. **Test with Postman** - Import OpenAPI spec
