# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a **strategic planning and documentation repository** for the Lao Knowledge Hub (LKH) project—a proposed digital publication platform for Laos, modeled after Thailand's MEB Market but tailored for the Lao educational context. The repository contains no source code; it houses business strategy, implementation plans, and design specifications.

## Project Overview

**Vision:** Build Laos' first comprehensive digital publication platform for academic content.

**Target Partner:** National University of Laos (NUOL) - Primary content source through professor partnerships

**Business Model:**
- Revenue share: 70% to Author / 30% to Platform
- "White Glove" digitization service for professors
- Future: B2B e-library subscriptions, general literature expansion

## Document Index

| File | Purpose |
|------|---------|
| `docs/1-initial-strategy.md` | Executive summary, market analysis, problem/solution framework, implementation phases |
| `docs/2-web-implementation-plan.md` | Technical architecture, tech stack (Flutter, Next.js, FastAPI, Supabase), database schema, API design |
| `docs/3-meb-benchmarking-plan.md` | Systematic approach to learning from MEB Market (Thailand's e-book platform) |
| `docs/4-meb-benchmarking-report.md` | Detailed MEB Market research: features, user flows, UI patterns, pain points |
| `docs/5-lkh-educational-design.md` | UI/UX design specifications, color palette, typography (Lao fonts), wireframes |

## Technology Stack (Planned)

| Layer | Technology |
|-------|------------|
| Client (Web + Mobile) | Flutter |
| Public Web (SEO) | Next.js 14+ |
| Backend Framework | Python + FastAPI |
| Backend-as-a-Service | Supabase (PostgreSQL, Auth, Storage) |
| PDF Rendering | syncfusion_flutter_pdfviewer |
| Authentication | Supabase Auth |
| Payments | BCEL One (OnePay) API |
| Hosting | Firebase Hosting |

## Key Design Decisions

### What to Adapt from MEB Market
- User journey patterns (browse → preview → buy → read)
- Book detail page layout (cover, description, TOC, reviews)
- PDF reader features (annotations, cloud sync, offline reading)
- Multiple payment methods approach

### What to Differentiate from MEB Market
- **Target audience:** Students/professors (not general readers)
- **Content:** Academic textbooks (not novels/comics)
- **Discovery:** By university, course, subject (not bestsellers)
- **Reading tools:** Study-focused (notes, citations, export)
- **Pricing:** Student discounts, semester rentals
- **Onboarding:** Minimal signup (5 fields vs MEB's 9)
- **Browsing:** Free browsing (no login wall)

### Lao Language Optimization
- Default font: Phetsarath OT
- Buttons and UI elements must be taller to accommodate Lao text (upper/lower vowels take more vertical space)
- Terminology shift: "Best Sellers" → "Most Popular", "Buy Now" → "Get Access"

## Development Phases

### Phase 1 (MVP - Weeks 1-8)
- Browse without login
- Category browsing, search with filters
- Book detail page with sample/preview
- Shopping cart and checkout
- PDF reader with annotations
- Cloud sync, offline reading
- User authentication

### Phase 2 (Weeks 9-16)
- Reviews & ratings
- Professor profiles
- University/course filters
- Rental option (50% price, 1 semester)
- Institutional purchase
- Annotation export, citation tools

### Phase 3 (Weeks 17-24)
- Subscription model (university libraries)
- Gift codes, loyalty credits
- Social reading (study groups)
- University LMS integration
- Audiobook support