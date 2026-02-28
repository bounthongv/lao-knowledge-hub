# Lao Knowledge Hub - Qwen Context

**Last Updated:** 2026-02-25  
**Project Status:** Backend & Flutter Setup Complete - Ready for Testing

---

## Project Overview

**Lao Knowledge Hub (LKH)** is a digital publication platform for Laos, inspired by Thailand's MEB Market, designed specifically for academic content from the National University of Laos (NUOL).

### Vision
Build Laos' first comprehensive digital publication platform—an ecosystem for Lao language content and Lao academic curricula.

### Target Users
- **Students** - Affordable access to textbooks
- **Professors** - Revenue share from digitized materials
- **Universities** - B2B e-library subscriptions

---

## Documentation Status

### ✅ Completed Documents

| # | Document | Description | Status |
|---|----------|-------------|--------|
| 1 | [1-initial-strategy.md](docs/1-initial-strategy.md) | Executive summary, market analysis, problem/solution | ✅ Complete |
| 2 | [2-web-implementation-plan.md](docs/2-web-implementation-plan.md) | Technology stack, database schema, API endpoints | ✅ Complete |
| 3 | [3-meb-benchmarking-plan.md](docs/3-meb-benchmarking-plan.md) | Plan for benchmarking MEB Market platform | ✅ Complete |
| 4 | [4-meb-benchmarking-report.md](docs/4-meb-benchmarking-report.md) | Comprehensive MEB Market analysis | ✅ Complete |
| 5 | [5-lkh-educational-design.md](docs/5-lkh-educational-design.md) | UI/UX design specification | ✅ Complete |
| 6 | [6-database-schema.md](docs/6-database-schema.md) | Complete Supabase database schema with RLS | ✅ Complete |
| 7 | [7-api-specification.md](docs/7-api-specification.md) | Full REST API specification | ✅ Complete |
| 8 | [8-user-flow-diagrams.md](docs/8-user-flow-diagrams.md) | Visual user flow diagrams | ✅ Complete |
| 9 | [9-supabase-setup-guide.md](docs/9-supabase-setup-guide.md) | Step-by-step Supabase configuration | ✅ Complete |
| 10 | [10-fastapi-setup-guide.md](docs/10-fastapi-setup-guide.md) | FastAPI backend setup guide | ✅ Complete |
| 11 | [11-implementation-checklist.md](docs/11-implementation-checklist.md) | Master implementation checklist | ✅ Complete |

---

## Project Structure

```
lao-knowledge-hub/
├── backend/                    # FastAPI Backend
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py            # FastAPI app entry point
│   │   ├── config.py          # Configuration
│   │   ├── database.py        # Supabase client
│   │   ├── models/            # Pydantic models
│   │   │   ├── users.py
│   │   │   ├── books.py
│   │   │   ├── orders.py
│   │   │   └── annotations.py
│   │   ├── routes/            # API routes
│   │   │   ├── auth.py
│   │   │   ├── books.py
│   │   │   ├── payments.py
│   │   │   ├── annotations.py
│   │   │   └── progress.py
│   │   └── middleware/
│   │       └── auth.py        # JWT authentication
│   ├── .env.example
│   ├── requirements.txt
│   └── README.md
│
├── flutter-app/               # Flutter Application
│   ├── lib/
│   │   ├── main.dart          # App entry point
│   │   ├── config/
│   │   │   ├── constants.dart
│   │   │   └── theme.dart
│   │   ├── models/
│   │   │   ├── book.dart
│   │   │   ├── user.dart
│   │   │   ├── order.dart
│   │   │   └── annotation.dart
│   │   ├── services/
│   │   │   ├── auth_service.dart
│   │   │   ├── api_service.dart
│   │   │   └── storage_service.dart
│   │   ├── providers/
│   │   │   ├── auth_provider.dart
│   │   │   ├── book_provider.dart
│   │   │   └── cart_provider.dart
│   │   └── screens/
│   │       ├── home/
│   │       ├── browse/
│   │       ├── book_detail/
│   │       ├── reader/
│   │       ├── library/
│   │       ├── auth/
│   │       └── profile/
│   ├── pubspec.yaml
│   └── README.md
│
└── docs/                      # Documentation
    ├── 1-initial-strategy.md
    ├── 2-web-implementation-plan.md
    ├── 3-meb-benchmarking-plan.md
    ├── 4-meb-benchmarking-report.md
    ├── 5-lkh-educational-design.md
    ├── 6-database-schema.md
    ├── 7-api-specification.md
    ├── 8-user-flow-diagrams.md
    ├── 9-supabase-setup-guide.md
    ├── 10-fastapi-setup-guide.md
    └── 11-implementation-checklist.md
```

---

## Technology Stack (Finalized)

| Layer | Technology | Status |
|-------|------------|--------|
| **Client (Web + Mobile)** | Flutter | ✅ Project created |
| **Public Web (SEO)** | Next.js 14+ | ⏳ Pending |
| **Backend Framework** | Python + FastAPI | ✅ Project created |
| **Backend-as-a-Service** | Supabase | ✅ Schema deployed |
| **File Storage** | Supabase Storage | ✅ Buckets configured |
| **PDF Rendering** | `syncfusion_flutter_pdfviewer` | ⏳ Pending |
| **Authentication** | Supabase Auth | ✅ Configured |
| **Payments** | BCEL One API | ⏳ Pending |
| **Hosting** | Firebase Hosting | ⏳ Pending |
| **Admin Dashboard** | React Admin + Supabase | ⏳ Pending |

---

## Implementation Progress

### ✅ Completed (2026-02-25)

#### Database & Infrastructure
- [x] Supabase project created
- [x] All 18 tables created (profiles, books, orders, annotations, etc.)
- [x] All RLS policies configured
- [x] All functions and triggers created
- [x] All indexes created for performance
- [x] Storage buckets configured (4 buckets)
- [x] Seed data inserted (universities, faculties, categories, courses)

#### Backend API (FastAPI)
- [x] Project structure created
- [x] Configuration management (`config.py`)
- [x] Supabase client setup (`database.py`)
- [x] Pydantic models (users, books, orders, annotations)
- [x] Authentication middleware (JWT verification)
- [x] API routes implemented:
  - [x] Authentication (`/api/v1/auth`)
  - [x] Books (`/api/v1/books`)
  - [x] Payments (`/api/v1/payments`)
  - [x] Annotations (`/api/v1/annotations`)
  - [x] Reading Progress (`/api/v1/progress`)
- [x] Requirements.txt with all dependencies

#### Flutter App
- [x] Project structure created
- [x] Pubspec.yaml with dependencies
- [x] Configuration (constants, theme)
- [x] Models (Book, User, Order, Annotation)
- [x] Services (Auth, API, Storage)
- [x] Providers (Auth, Book, Cart)
- [x] Screens (placeholders):
  - [x] Home screen
  - [x] Browse screen
  - [x] Book detail screen
  - [x] Reader screen
  - [x] Library screen
  - [x] Login screen
  - [x] Register screen
  - [x] Profile screen
  - [x] Cart screen

---

## Next Steps (Immediate)

### This Week
- [ ] **Configure Supabase credentials**
  - Update `backend/.env` with your Supabase URL and keys
  - Update `flutter-app/lib/config/constants.dart` with Supabase URL and anon key

- [ ] **Test Backend API**
  ```bash
  cd backend
  python -m venv venv
  venv\Scripts\activate  # Windows
  pip install -r requirements.txt
  uvicorn app.main:app --reload
  ```
  - Visit http://localhost:8000/docs
  - Test `/health` endpoint
  - Test `/api/v1/books` endpoint

- [ ] **Test Flutter App**
  ```bash
  cd flutter-app
  flutter pub get
  flutter run -d chrome
  ```
  - Test login/register flows
  - Test home screen display

### Week 2-3
- [ ] **Implement remaining Flutter screens**
  - Book detail screen with full data
  - PDF reader with annotations
  - Shopping cart and checkout
  - Library with reading progress

- [ ] **Integrate backend with Flutter**
  - Connect auth service to Supabase
  - Connect book provider to API
  - Implement real-time data sync

### Week 4-6
- [ ] **BCEL Payment Integration**
  - Contact BCEL for API credentials
  - Implement payment service
  - Test payment flow

- [ ] **Deploy to Production**
  - Deploy backend to Firebase Cloud Run
  - Deploy Flutter web to Firebase Hosting
  - Configure production Supabase

---

## Key Decisions Made

| Decision | Rationale |
|----------|-----------|
| **Flutter for cross-platform** | Single codebase, reduces dev time 50%+ |
| **Supabase for backend** | 80% of backend out-of-the-box, reduces boilerplate |
| **Next.js for SEO** | Public book catalog must be Google-indexable |
| **FastAPI for custom logic** | Payments, DRM, royalties need custom implementation |
| **PDF-first approach** | Professors already have content in PDF/Word |
| **BCEL One for payments** | Local payment method, widely used in Laos |
| **70/30 royalty split** | Competitive with MEB, incentivizes professors |
| **Rental option (50% price)** | Student-friendly pricing for semester access |
| **Simplified registration (5 fields)** | Reduce friction vs MEB (9 fields) |
| **Browse without login** | Allow discovery before commitment |

---

## Risk Mitigation

| Risk | Mitigation Strategy |
|------|---------------------|
| **Professor adoption** | "White Glove" digitization service, no upfront cost |
| **Payment integration** | Start with manual bank transfer fallback |
| **DRM/piracy** | Social watermarking, device limits (3 devices) |
| **Low internet speeds** | Offline reading, optimized PDF compression |
| **Content quality** | Admin review process before publishing |
| **Student affordability** | Rental option, institutional purchases |

---

## Success Metrics (MVP Launch)

| Metric | Target (3 months) |
|--------|-------------------|
| Registered users | 500+ |
| Published books | 50+ |
| Monthly active users | 200+ |
| Conversion rate | 5%+ |
| Average order value | 40,000 LAK |
| User retention (30-day) | 40%+ |

---

## Related Resources

- **Supabase Project:** https://app.supabase.com
- **MEB Market:** https://www.mebmarket.com
- **Flutter:** https://flutter.dev
- **FastAPI:** https://fastapi.tiangolo.com
- **BCEL:** https://www.bcel.com.la

---

## Notes for Next Session

When continuing work:
1. Reference this QWEN.md for project context
2. Check docs/ folder for completed documentation
3. Backend and Flutter projects are set up and ready
4. Next priority: Test backend API and Flutter app
5. Then: Implement remaining screens and features
6. Maintain educational design aesthetic (not commercial)
7. Prioritize Lao language optimization (Phetsarath OT font)
