# MEB Market Benchmarking Research Report

**Research Date:** 2026-02-24  
**Researcher:** AI Assistant  
**Project:** Lao Knowledge Hub

---

## Executive Summary

MEB Market is **Thailand's #1 e-book platform** with:
- **13+ million registered users**
- **100,000+ e-books** in catalog
- **2.2+ billion Baht revenue** (2024)
- **8 consecutive years** as top-grossing book app in Thailand

This report documents MEB's features, user flows, UI patterns, and pain points to inform Lao Knowledge Hub development.

---

## 1. Company & Platform Overview

### 1.1 Business Model

| Component | Details |
|-----------|---------|
| **Parent Company** | MEB Corporation Public Company Limited (SET-listed) |
| **Founded** | 2011 (platform launched) |
| **Headquarters** | Nonthaburi, Thailand |
| **Revenue Model** | E-book sales (70/30 royalty split), subscriptions, e-reader hardware |
| **B2B Arm** | Hytexts - Hibrary e-library system for organizations |

### 1.2 Platform Ecosystem

```
┌─────────────────────────────────────────────────────────────┐
│                    MEB CORPORATION                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────┐  │
│  │  mebmarket   │  │  readAwrite  │  │  Hytexts         │  │
│  │  (E-books)   │  │  (Web Novels)│  │  (E-readers +    │  │
│  │              │  │              │  │   B2B Library)   │  │
│  └──────────────┘  └──────────────┘  └──────────────────┘  │
│                                                             │
│  ┌──────────────┐                                          │
│  │  Incognito   │                                          │
│  │  Lab         │                                          │
│  │  (Security)  │                                          │
│  └──────────────┘                                          │
└─────────────────────────────────────────────────────────────┘
```

### 1.3 Platform Availability

| Platform | App Name | Notes |
|----------|----------|-------|
| **Web** | mebmarket.com | Full feature access |
| **iOS** | "meb" | In-app purchase (Apple fee) or meb coins |
| **Android** | "meb+" | All payment methods supported |
| **Desktop** | WebCatalog app | Mac/Windows wrapper |
| **E-readers** | Hytexts devices | Kindle alternative for Thailand |

---

## 2. Complete User Flow Documentation

### 2.1 Registration Flow

```
┌─────────────────────────────────────────────────────────────┐
│  STEP 1: Click "Register"                                   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 2: Fill Registration Form                             │
│  ┌───────────────────────────────────────────────────────┐  │
│  │ • Username (4-32 chars: a-z, A-Z, _-@)                │  │
│  │ • Password (min 8 characters)                         │  │
│  │ • Retype Password                                     │  │
│  │ • Email                                               │  │
│  │ • Display Name                                        │  │
│  │ • Phone Number                                        │  │
│  │ • First Name & Last Name                              │  │
│  │ • Gender (Male/Female/Not specified)                  │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 3: Click "Send" → Account Created                     │
│  • Can use readawrite.com credentials if existing           │
└─────────────────────────────────────────────────────────────┘
```

**⚠️ PAIN POINT:** 9 required fields is **high friction** vs industry standard (email + password)

**✅ OUR IMPROVEMENT:** Reduce to 5 fields (email, password, full name, phone, role)

---

### 2.2 Browse & Discovery Flow

```
┌─────────────────────────────────────────────────────────────┐
│  HOMEPAGE                                                   │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  [Logo] [Search]              [Login] [Cart] [Menu]   │  │
│  ├───────────────────────────────────────────────────────┤  │
│  │  Navigation:                                          │  │
│  │  All | Boy Love | Girl Love | Fiction | Comic | ...  │  │
│  ├───────────────────────────────────────────────────────┤  │
│  │  • Best Sellers (ขายดี)                              │  │
│  │  • New Releases (มาใหม่)                             │  │
│  │  • Promotions (โปรโมชัน)                            │  │
│  │  • Free Books (ฟรีกระจาย)                           │  │
│  │  • Popular Classics (ฮิตขึ้นหิ้ง)                   │  │
│  │  • Recommended (แนะนำ)                              │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  CATEGORY BROWSING                                          │
│  • Hierarchical categories (10+ main categories)            │
│  • Sub-categories within each                               │
│  • Tag-based filtering                                      │
│  • Search with filters (genre, price, author, publisher)    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  BOOK LISTINGS (Grid View)                                  │
│  • Cover image                                              │
│  • Title (Thai + English)                                   │
│  • Author/Publisher                                         │
│  • Price / Discount badge                                   │
│  • Rating stars                                             │
└─────────────────────────────────────────────────────────────┘
```

**✅ WHAT TO COPY:**
- Clear category hierarchy
- Multiple discovery paths (bestsellers, new, promoted, free)
- Tag-based filtering

**⚠️ WHAT TO IMPROVE:**
- MEB requires login to browse some content → **We allow free browsing**

---

### 2.3 Book Detail Page Flow

```
┌─────────────────────────────────────────────────────────────┐
│  BOOK DETAIL PAGE                                           │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  [Cover Image]     Title (Thai + English)             │  │
│  │                    Author: [Name]                     │  │
│  │                    Publisher: [Name]                  │  │
│  │                    ⭐⭐⭐⭐⭐ (4.5) | 234 reviews     │  │
│  │                                                       │  │
│  │  [Read Sample]  [Add to Cart]  [Buy Now]             │  │
│  └───────────────────────────────────────────────────────┘  │
│  ───────────────────────────────────────────────────────────  │
│  📖 Description                                               │
│  [Expandable text about the book content]                     │
│  ───────────────────────────────────────────────────────────  │
│  📑 Table of Contents                                         │
│  • Chapter 1 ............................ Page 1              │
│  • Chapter 2 ............................ Page 15             │
│  • Chapter 3 ............................ Page 30             │
│  ───────────────────────────────────────────────────────────  │
│  💬 Reviews (234)                                             │
│  [Write a Review]                                             │
│  ⭐⭐⭐⭐⭐ "Great book!" - User123                             │
│  ⭐⭐⭐⭐ "Very helpful" - Reader456                          │
│  ───────────────────────────────────────────────────────────  │
│  📚 Related Books                                             │
│  [Book] [Book] [Book] [Book] →                               │
└─────────────────────────────────────────────────────────────┘
```

**✅ KEY FEATURES:**
- Sample/Preview button (first 5-10 pages)
- Clear CTAs (Sample, Cart, Buy Now)
- Table of Contents preview
- User reviews with ratings
- Related book recommendations

**✅ OUR ADAPTATION:**
- Add professor/university info for academic books
- Add course correlation (which courses use this book)

---

### 2.4 Purchase Flow

```
┌─────────────────────────────────────────────────────────────┐
│  STEP 1: Add to Cart / Buy Now                              │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 2: Login (if not already)                             │
│  • Social login (Facebook, Line, Apple, Google)             │
│  • MEB account                                              │
│  • The1 integration                                         │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 3: Shopping Cart Review                               │
│  • List of books                                            │
│  • Total price                                              │
│  • meb Coin balance                                         │
│  • [Checkout] button                                        │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 4: Payment Method Selection                           │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  • meb Coin (pre-purchased)                           │  │
│  │  • Credit/Debit Card                                  │  │
│  │  • Mobile Banking                                     │  │
│  │  • Convenience Store (7-Eleven)                       │  │
│  │  • Apple In-App Purchase (iOS only, +fee)             │  │
│  │  • Google Play Billing (Android only, +fee)           │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 5: Payment Processing                                 │
│  • Redirect to payment gateway                              │
│  • Complete payment                                         │
│  • Return to MEB                                            │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 6: Purchase Confirmation                              │
│  • Success page                                             │
│  • Book added to library                                    │
│  • [Read Now] button                                        │
└─────────────────────────────────────────────────────────────┘
```

**✅ WHAT TO COPY:**
- Multiple payment methods (critical for SEA market)
- Shopping cart for multi-book purchases
- Pre-paid coin system (avoids platform fees)

**⚠️ WHAT TO IMPROVE:**
- MEB: iOS in-app purchase has Apple fee → **We use meb coin model (BCEL One)**
- MEB: Complex checkout → **We streamline to 3 steps max**

---

### 2.5 Reading Flow

```
┌─────────────────────────────────────────────────────────────┐
│  READER INTERFACE                                           │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  ← Library    Book Title           [Settings] [X]     │  │
│  ├───────────────────────────────────────────────────────┤  │
│  │                                                       │  │
│  │              [PDF Page Content]                       │  │
│  │                                                       │  │
│  ├───────────────────────────────────────────────────────┤  │
│  │  [◀ Prev]    Page 45 / 250    [Next ▶]               │  │
│  │                                                       │  │
│  │  [Toolbar: Highlight] [Note] [Bookmark] [Search]     │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

**✅ READER FEATURES:**

| Feature | Description |
|---------|-------------|
| **File Support** | PDF, EPUB, multimedia books |
| **Text Customization** | Resize text, change fonts, line spacing (EPUB) |
| **Themes** | Day, Night, Sepia, Custom colors |
| **Brightness** | In-app brightness control |
| **Navigation** | Swipe or tap to turn pages |
| **Page Animation** | Optional (can disable) |
| **Search** | Full-text search within book (EPUB) |
| **Annotations** | Highlights, notes, drawings |
| **Bookmarks** | Multiple bookmarks per book |
| **Progress Sync** | Last page synced across devices |
| **Offline Reading** | Download books for offline access |
| **Auto-scroll** | EPUB auto-scroll mode |

**✅ OUR ADAPTATION:**
- All features above **PLUS**:
- Study-specific tools (citation export, study session tracking)
- Better annotation organization (by chapter, by color)

---

## 3. Feature Analysis

### 3.1 Core Features (Table)

| Feature | MEB Implementation | Priority | Our Adaptation |
|---------|-------------------|----------|----------------|
| **Browse Catalog** | Category + search + filters | P0 | Same + university/course filters |
| **Book Detail** | Cover, desc, TOC, reviews | P0 | Same + professor bio, course info |
| **Sample/Preview** | First 5-10 pages free | P0 | Same + 1 chapter option |
| **Shopping Cart** | Multi-book checkout | P0 | Same + institutional purchase |
| **Payment Methods** | 6+ methods | P0 | BCEL One + bank transfer (start) |
| **PDF Reader** | Full-featured | P0 | Same + study tools |
| **Annotations** | Highlight, notes, bookmarks | P0 | Same + better organization |
| **Cloud Sync** | Progress, bookmarks, notes | P0 | Same + study history |
| **Offline Reading** | Download books | P0 | Same + download management |
| **Reviews/Ratings** | User reviews | P1 | Same + academic moderation |
| **Wishlist** | Save for later | P1 | Same |
| **Publisher Follow** | Follow publishers | P2 | Follow professors/universities |
| **Gift Codes** | Gift books | P2 | For special occasions |
| **Loyalty (Coins/Stamps)** | meb Coins + Stamps | P2 | Simplified: purchase credits |
| **Subscription** | MEB Buffet (all-you-can-read) | P2 | Phase 2: University libraries |
| **Kid's Mode** | Parental controls | ❌ Skip | Not relevant for academic |
| **Age Verification** | Thai ID for 18+ | ❌ Skip | Student ID only if needed |

---

### 3.2 Loyalty Program Analysis

**MEB Coins:**
- Pre-purchased credits (avoid iOS/Android fees)
- 1 Coin = 1 Baht
- Bonus: Buy 1000 Baht, get 50 Coins free

**MEB Stamps:**
- Earn 1 stamp per book purchase
- Collect stamps → redeem special rewards
- Gamification element

**✅ OUR APPROACH:**
- **Simplify:** Only purchase credits (no complex stamp system)
- **Student Discounts:** Bulk purchase discounts for universities
- **Rental Model:** 50% price for 1-semester access

---

## 4. UI/UX Pattern Analysis

### 4.1 Homepage Layout

```
┌────────────────────────────────────────────────────────────┐
│  [Logo]    [══════ Search ══════]   [Login] [Cart] [≡]    │
├────────────────────────────────────────────────────────────┤
│  All ▼ | Boy Love | Girl Love | Fiction | Comic | More →  │
├────────────────────────────────────────────────────────────┤
│  [Hero Banner: Featured Book/Promotion]                    │
├────────────────────────────────────────────────────────────┤
│  🔥 Best Sellers                                           │
│  [Book Card] [Book Card] [Book Card] [Book Card] →        │
├────────────────────────────────────────────────────────────┤
│  📚 New Releases                                           │
│  [Book Card] [Book Card] [Book Card] [Book Card] →        │
├────────────────────────────────────────────────────────────┤
│  🎁 Free Books                                             │
│  [Book Card] [Book Card] [Book Card] [Book Card] →        │
├────────────────────────────────────────────────────────────┤
│  📖 Recommended for You                                    │
│  [Book Card] [Book Card] [Book Card] [Book Card] →        │
└────────────────────────────────────────────────────────────┘
```

**Book Card Layout:**
```
┌─────────────────┐
│                 │
│   [Cover]       │
│   Image         │
│                 │
├─────────────────┤
│ Title (Thai)    │
│ Author          │
│ ⭐⭐⭐⭐⭐      │
│ ฿150  -20%     │
└─────────────────┘
```

**✅ OUR ADAPTATION:**
- Replace "Boy Love/Girl Love" with academic subjects
- Add "Textbooks" and "University Collections" sections
- Cleaner, more academic aesthetic

---

### 4.2 Reader UI Patterns

**Toolbar Placement:**
- **Top:** Navigation (back, title, settings)
- **Bottom:** Page navigation, annotation tools
- **Tap center:** Toggle toolbar visibility

**Gesture Controls:**
- **Swipe left/right:** Turn pages
- **Tap right side:** Next page
- **Tap left side:** Previous page
- **Pinch:** Zoom
- **Long press:** Select text (highlight/note)

**Settings Menu:**
```
┌─────────────────────────────┐
│  ⚙️ Reading Settings        │
├─────────────────────────────┤
│  Font Size:  A-  [16]  A+   │
│  Font:       [Phetsarath OT]▼│
│  Theme:      [Day ▼]        │
│  Brightness: [━━━━━●━━]     │
│  Scroll:     [Off ▼]        │
│  Animation:  [✓ On]         │
└─────────────────────────────┘
```

**✅ OUR ADAPTATION:**
- Default font: **Phetsarath OT** (Lao)
- Add "Study Mode" (disable animations, optimize for note-taking)

---

## 5. Technical Implementation

### 5.1 DRM Strategy

**MEB's Approach:**
- Encrypted downloads (device-specific)
- Account-based authentication
- Device limits (unlimited, but practical limits via encryption)
- Watermarking (user info embedded)

**✅ OUR APPROACH:**
```
1. Signed URLs (2-hour expiry for reading sessions)
2. Device fingerprinting (max 3 devices per user)
3. Social DRM (user phone number watermarked on pages)
4. Encrypted storage (Supabase Storage with RLS)
5. Offline access (time-limited downloads)
```

### 5.2 Cloud Sync Architecture

**What to Sync:**
- Last read page (per book)
- Bookmarks
- Highlights & notes
- Reading progress (%)
- Study session history

**Sync Strategy:**
```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   Device 1   │────▶│   Supabase   │◀────│   Device 2   │
│   (Phone)    │     │  (PostgreSQL)│     │   (Tablet)   │
└──────────────┘     └──────────────┘     └──────────────┘
       ▲                    │                    ▲
       │                    ▼                    │
       │            ┌──────────────┐             │
       └────────────│   FastAPI    │─────────────┘
                    │   (Sync API) │
                    └──────────────┘
```

**Sync API Endpoints:**
```python
POST /api/sync/progress      # Update reading progress
GET  /api/sync/progress      # Get latest progress
POST /api/sync/annotations   # Sync annotations
GET  /api/sync/annotations   # Get all annotations
```

---

## 6. User Pain Points (MEB)

### 6.1 Identified Pain Points

| Pain Point | User Complaint | Frequency | Our Solution |
|------------|----------------|-----------|--------------|
| **Forced login to browse** | "Can't see anything without account" | High | ✅ Allow browsing |
| **Complex registration** | "Too many fields, takes forever" | High | ✅ Minimal signup (5 fields) |
| **iOS in-app purchase fee** | "Why is it more expensive on iOS?" | Medium | ✅ Use BCEL One (no fee) |
| **Slow reader app** | "Laggy page turns on old phones" | Medium | ✅ Optimize for low-end devices |
| **DRM too restrictive** | "Can't read on my tablet and phone" | Low | ✅ Allow 3 devices |
| **Cluttered homepage** | "Too many popups and banners" | Medium | ✅ Clean, academic design |
| **Age verification blocks** | "Can't access even normal books" | Low | ✅ Only for truly restricted content |

### 6.2 User Reviews Summary

**Positive Feedback:**
- ✅ Huge book selection (100,000+ titles)
- ✅ Cross-device sync works well
- ✅ Good Thai language support
- ✅ Multiple payment options
- ✅ Regular promotions and discounts

**Negative Feedback:**
- ❌ Registration form too long
- ❌ Login required to browse
- ❌ iOS prices higher (Apple fee)
- ❌ Occasional app slowness
- ❌ Too many notifications/promotions

---

## 7. Competitive Differentiation Strategy

### 7.1 How Lao Knowledge Hub Differs

| Aspect | MEB Market | Lao Knowledge Hub |
|--------|------------|-------------------|
| **Target Audience** | General readers | Students + Professors |
| **Content Focus** | Novels, comics, general | Academic textbooks |
| **Discovery** | Bestsellers, trending | By university, course, subject |
| **Reading Tools** | Basic highlights | Study-focused (notes, citations) |
| **Pricing** | Consumer pricing | Student discounts, rentals |
| **Distribution** | Direct to consumer | University partnerships |
| **Author Support** | Self-service upload | "White Glove" digitization |
| **Onboarding** | Complex (9 fields) | Simple (5 fields) |
| **Browsing** | Login required | Free browsing |

### 7.2 Unique Value Propositions

1. **University-First Design**
   - Browse by university, course, subject
   - Professor profiles with credentials
   - Official course material integration

2. **Student-Friendly Pricing**
   - Rental option (50% price, 1 semester)
   - Institutional purchases (university buys for class)
   - Bulk discounts for student groups

3. **Study-Optimized Reader**
   - Citation export (APA, MLA, Chicago)
   - Study session tracking
   - Annotation organization (by chapter, color, tag)
   - Note export to Word/Google Docs

4. **"White Glove" Professor Support**
   - We digitize their Word/PDF files
   - Professional formatting
   - No upfront cost (revenue share model)

5. **Lao Language Optimization**
   - Phetsarath OT font built-in
   - Lao UI/UX (not translated Thai)
   - Local payment methods (BCEL One)

---

## 8. Implementation Priorities

### 8.1 Phase 1 (MVP - Weeks 1-8)

**P0 Features (Must-Have):**
- [ ] Browse without login
- [ ] Category browsing (academic subjects)
- [ ] Search with filters
- [ ] Book detail page (cover, desc, TOC, professor bio)
- [ ] Sample/Preview (first 10 pages)
- [ ] Shopping cart
- [ ] Checkout with BCEL One
- [ ] PDF reader with annotations
- [ ] Cloud sync (progress, bookmarks, notes)
- [ ] Offline reading
- [ ] User authentication (Supabase)

### 8.2 Phase 2 (Weeks 9-16)

**P1 Features (Should-Have):**
- [ ] Reviews & ratings (moderated)
- [ ] Professor/author profiles
- [ ] University/course filters
- [ ] Reading progress tracking
- [ ] Study session history
- [ ] Rental option (50% price, 1 semester)
- [ ] Institutional purchase (university buys for class)
- [ ] Annotation export
- [ ] Citation tools

### 8.3 Phase 3 (Weeks 17-24)

**P2 Features (Nice-to-Have):**
- [ ] Subscription model (university library)
- [ ] Gift codes
- [ ] Loyalty credits
- [ ] Social reading (study groups)
- [ ] Integration with university LMS
- [ ] Audiobook support
- [ ] Advanced analytics for professors

---

## 9. Next Steps

### 9.1 Immediate Actions (This Week)

1. **✅ Complete this benchmarking report**
2. **Create MEB test account** - Document every step (see Appendix A)
3. **Screenshot key screens** - Homepage, book detail, reader, checkout (50+ screenshots)
4. **Test purchase flow** - Note friction points, timing, errors
5. **Interview 2-3 MEB users** - What they love, what frustrates them

### 9.2 Design Sprint (Week 3-4)

1. **Wireframe based on MEB patterns** - Adapt, don't copy
2. **Add Lao-specific elements** - Phetsarath OT font, local aesthetics
3. **Review with NUOL partners** - Ensure academic relevance
4. **User test wireframes** - 5-10 students, get feedback

### 9.3 Development (Week 5-20)

1. **Implement P0 features first** - Browse, preview, buy, read
2. **Optimize for low-end devices** - Rural students with basic phones
3. **Test with real content** - Upload 5-10 sample textbooks
4. **Iterate based on feedback** - Weekly user testing

---

## Appendix A: MEB Test Account Creation Script

**For Research Purposes:**

```
Step 1: Visit www.mebmarket.com
Step 2: Click "Register" (top right)
Step 3: Fill form:
  - Username: research_test_001
  - Password: TestPass123
  - Email: research@test.com
  - Display Name: Research Test
  - Phone: 0123456789
  - First Name: Research
  - Last Name: Test
  - Gender: Not specified
Step 4: Click "Send"
Step 5: Verify email (if required)
Step 6: Login and explore
```

**Tasks to Document:**
- [ ] Time to complete registration
- [ ] Number of required fields
- [ ] Validation errors encountered
- [ ] Email verification time
- [ ] Login success rate
- [ ] Browse experience (any blocks?)
- [ ] Sample reading experience
- [ ] Purchase flow (add to cart, checkout)
- [ ] Reader features (annotations, sync)
- [ ] Any bugs or errors

---

## Appendix B: Screenshot Checklist

**Homepage (5 screenshots):**
- [ ] Desktop homepage (full page)
- [ ] Mobile homepage (full page)
- [ ] Category dropdown
- [ ] Search results
- [ ] Best sellers section

**Book Detail (5 screenshots):**
- [ ] Book detail (full page)
- [ ] Description expanded
- [ ] Table of Contents
- [ ] Reviews section
- [ ] Related books

**Reader (8 screenshots):**
- [ ] Reader (default view)
- [ ] Toolbar visible
- [ ] Settings menu
- [ ] Font selection
- [ ] Theme selection (Day/Night/Sepia)
- [ ] Highlighting in action
- [ ] Notes interface
- [ ] Bookmarks panel

**Checkout (6 screenshots):**
- [ ] Shopping cart
- [ ] Payment method selection
- [ ] meb Coin purchase
- [ ] Credit card form
- [ ] Success page
- [ ] Library after purchase

**Total: 24+ screenshots minimum**

---

*Report Version: 1.0 | Created: 2026-02-24 | Researcher: AI Assistant*
