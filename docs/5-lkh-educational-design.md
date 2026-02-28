# Lao Knowledge Hub - Educational UI/UX Design Specification

**Version:** 1.0  
**Date:** 2026-02-24  
**Inspired by:** MEB Market (adapted for academic use)  
**Design Philosophy:** Educational, Trustworthy, Student-Friendly

---

## 1. Design Philosophy Shift

### From Commercial (MEB) → Educational (Lao Knowledge Hub)

| Aspect | MEB (Commercial) | Lao Knowledge Hub (Educational) |
|--------|------------------|--------------------------------|
| **Tone** | Exciting, promotional | Trustworthy, academic |
| **Colors** | Vibrant, sales-oriented | Calm, study-focused |
| **Language** | "Best Selling", "Hot", "Promotion" | "Most Popular", "Recommended", "Required" |
| **Imagery** | Book covers, promotions | Campus, students studying, professors |
| **Urgency** | "Limited time offer!" | "Required for your course" |
| **Social Proof** | Sales numbers, ratings | Professor endorsements, university adoption |

---

## 2. Terminology Changes

### Commercial → Educational Language

| Commercial Term (Thai) | Educational Replacement (Lao) | Rationale |
|-----------------|------------------------|-----------|
| **Best Sellers** (ຂາຍດີ) | **Most Popular** (ນິຍົມທີ່ສຸດ) | Sales ≠ academic value |
| **Hot Books** (ໜັງສືຮິດ) | **Trending in Your Field** (ກຳລັງນິຍົມໃນສາຂາຂອງທ່ານ) | Academic relevance over hype |
| **Promotions** (ໂປຣໂມຊັ່ນ) | **Student Discounts** (ສ່ວນຫຼຸດນັກຮຽນ) | Discount = student benefit |
| **Free Books** (ຟຣີ) | **Open Access** (ເປີດເຂົ້າເຖິງ) | Academic term for free resources |
| **New Releases** (ມາໃໝ່) | **Recently Added** (ເພີ່ມໃໝ່) | Less commercial, more informational |
| **Recommended** (ແນະນຳ) | **Faculty Recommendations** (ຄະນະແນະນຳ) | Authority-based recommendation |
| **Top Rated** (ຄະແນນສູງສຸດ) | **Highly Rated** (ໃຫ້ຄະແນນສູງ) | Less hype, more descriptive |
| **Must Read** (ຕ້ອງອ່ານ) | **Required Reading** (ອ່ານບັງຄັບ) | Academic standard term |
| **Buy Now** (ຊື້ເລີຍ) | **Get Access** (ເຂົ້າເຖິງ) | Less transactional |
| **Add to Cart** (ໃສ່ຕະກຣ້າ) | **Add to List** (ເພີ່ມໃສ່ລາຍການ) | Less commercial |
| **Checkout** (ຊຳລະເງິນ) | **Continue** (ຕໍ່ໄປ) | Process-focused, not payment-focused |
| **Limited Offer** (ຂໍ້ສະເໜີຈຳກັດ) | **Semester Access** (ເຂົ້າເຖິງພາກຮຽນ) | Time-bound for academic reasons |
| **Premium** (ພຣີມຽມ) | **Full Access** (ເຂົ້າເຖິງເຕັມ) | Feature-focused, not status |
| **VIP** (ວີໄອພີ) | **Institutional Access** (ເຂົ້າເຖິງສະຖາບັນ) | University partnership focus |

---

## 3. Color Palette

### MEB (Commercial) vs. Our (Educational)

**MEB Colors:**
- Primary: Bright Orange/Red (#FF6B35) - Urgency, sales
- Secondary: Bright Blue - Tech, modern
- Accent: Yellow/Gold - Premium, rewards

**Lao Knowledge Hub Colors:**
```
Primary Colors:
┌─────────────────────────────────────────────────────┐
│  Deep Blue: #1E3A8A    (Trust, knowledge, NUOL)    │
│  Navy: #1E40AF         (Academic, professional)     │
│  White: #FFFFFF        (Clean, clarity)             │
└─────────────────────────────────────────────────────┘

Secondary Colors:
┌─────────────────────────────────────────────────────┐
│  Lao Red: #DC2626      (National pride, emphasis)  │
│  Gold: #F59E0B         (Excellence, achievement)   │
│  Green: #059669        (Growth, learning)          │
└─────────────────────────────────────────────────────┘

Neutral Colors:
┌─────────────────────────────────────────────────────┐
│  Gray 100: #F3F4F6   (Backgrounds)                 │
│  Gray 300: #D1D5DB   (Borders, dividers)           │
│  Gray 500: #6B7280   (Secondary text)              │
│  Gray 700: #374151   (Primary text)                │
│  Gray 900: #111827   (Headings)                    │
└─────────────────────────────────────────────────────┘

Semantic Colors:
┌─────────────────────────────────────────────────────┐
│  Success: #10B981    (Completed, available)        │
│  Warning: #F59E0B    (Limited time, expiring)      │
│  Error: #EF4444      (Error, expired)              │
│  Info: #3B82F6       (Information, tips)           │
└─────────────────────────────────────────────────────┘
```

### Color Usage Guidelines

| Element | Color | Usage |
|---------|-------|-------|
| **Primary Buttons** | Deep Blue (#1E3A8A) | Main CTAs (Get Access, Continue) |
| **Secondary Buttons** | White with Blue Border | Secondary actions (Read Sample, Add to List) |
| **Links** | Navy (#1E40AF) | Navigation, internal links |
| **Success States** | Green (#059669) | Purchase complete, download ready |
| **Warnings** | Gold (#F59E0B) | Rental expiring soon, limited copies |
| **Badges** | Varies | "Required", "Recommended", "Open Access" |

---

## 4. Typography

### Font Stack

**Primary Font (Lao):**
```
Phetsarath OT
- Headings: 24px, 20px, 18px
- Body: 16px
- Small: 14px
- Line height: 1.6 (readability optimized)
```

**Secondary Font (English):**
```
Inter / System UI
- Headings: Same as above
- Body: Same as above
- Code: 14px monospace
```

### Typography Hierarchy

```
┌─────────────────────────────────────────────────────┐
│  H1: Page Title                                     │
│  Phetsarath OT, 32px, Bold (#111827)               │
│  ສູນຄວາມຮູ້ລາວ                                       │
├─────────────────────────────────────────────────────┤
│  H2: Section Heading                                │
│  Phetsarath OT, 24px, Semi-Bold (#111827)          │
│  ປຶ້ມທີ່ນິຍົມທີ່ສຸດ                               │
├─────────────────────────────────────────────────────┤
│  H3: Card Title                                     │
│  Phetsarath OT, 18px, Semi-Bold (#1F2937)          │
│  ພື້ນຖານການບັນຊີ                                  │
├─────────────────────────────────────────────────────┤
│  Body: Main Content                                 │
│  Phetsarath OT, 16px, Regular (#374151)            │
│  Line height: 1.6, Letter spacing: 0.02em          │
├─────────────────────────────────────────────────────┤
│  Small: Metadata, Captions                          │
│  Phetsarath OT, 14px, Regular (#6B7280)            │
│  Author, University, Year                          │
└─────────────────────────────────────────────────────┘
```

---

## 5. Homepage Design (Educational Adaptation)

### 5.1 Layout Comparison

**MEB Homepage (Commercial):**
```
┌────────────────────────────────────────────────────┐
│  [Logo] [Search]          [Login] [Cart] [Menu]   │
├────────────────────────────────────────────────────┤
│  All ▼ | Boy Love | Girl Love | Fiction | Comic  │
├────────────────────────────────────────────────────┤
│  [HERO BANNER: "50% OFF - LIMITED TIME!"]         │
├────────────────────────────────────────────────────┤
│  🔥 BEST SELLERS (sales-focused)                  │
│  [Book] [Book] [Book] [Book] →                   │
├────────────────────────────────────────────────────┤
│  🎁 FREE BOOKS (promotional)                      │
│  [Book] [Book] [Book] [Book] →                   │
└────────────────────────────────────────────────────┘
```

**Lao Knowledge Hub Homepage (Educational):**
```
┌────────────────────────────────────────────────────┐
│  [NUOL Logo] [Search]      [Login] [Library] [≡] │
├────────────────────────────────────────────────────┤
│  Browse ▼ | Sciences | Arts | Engineering | Law  │
├────────────────────────────────────────────────────┤
│  [HERO: "Welcome to Lao Knowledge Hub"]           │
│  "Access 10,000+ academic resources from NUOL"    │
│  [Browse Catalog] [My Courses]                    │
├────────────────────────────────────────────────────┤
│  📚 MOST POPULAR THIS SEMESTER (academic focus)   │
│  [Textbook] [Textbook] [Textbook] [Textbook] →   │
├────────────────────────────────────────────────────┤
│  🎓 FACULTY RECOMMENDATIONS (authority-based)     │
│  [Book] [Book] [Book] [Book] →                   │
├────────────────────────────────────────────────────┤
│  📖 REQUIRED FOR YOUR COURSES (personalized)      │
│  [Book] [Book] [Book] →                          │
├────────────────────────────────────────────────────┤
│  🔓 OPEN ACCESS RESOURCES (free academic)         │
│  [Paper] [Paper] [Paper] [Paper] →               │
└────────────────────────────────────────────────────┘
```

### 5.2 Detailed Homepage Wireframe

```
┌──────────────────────────────────────────────────────────────────┐
│  HEADER                                                          │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │ [🎓 LKH]  ສູນຄວາມຮູ້ລາວ    [🔍 ຄົ້ນຫາ...]  [📚 ຫໍ້ສະໝຸດ] [👤] │ │
│  └────────────────────────────────────────────────────────────┘ │
├──────────────────────────────────────────────────────────────────┤
│  NAVIGATION                                                      │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │ ທັງໝົດ ▼  ວິທະຍາສາດ  ວິທະຍາສາດສັງຄົມ  ວິສະວະກຳ  ນິຕິສາດ     │ │
│  │          ແພດສາດ  ກະສິກຳ  ສຶກສາສາດ  ທຸກສາຂາ →  │ │
│  └────────────────────────────────────────────────────────────┘ │
├──────────────────────────────────────────────────────────────────┤
│  HERO SECTION                                                    │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │                                                              │ │
│  │   ຍິນດີຕ້ອນຮັບສູ່ ສູນຄວາມຮູ້ລາວ                              │ │
│  │   ເຂົ້າເຖິງຊັບພະຍາກອນການສຶກສາກວ່າ 10,000+ ຈາກ ມຊ           │ │
│  │                                                              │ │
│  │   [📖 ຊອກຫາປຶ້ມ]  [📋 ວິຊາຂອງຂ້ອຍ]                      │ │
│  │                                                              │ │
│  └────────────────────────────────────────────────────────────┘ │
├──────────────────────────────────────────────────────────────────┤
│  SECTION 1: MOST POPULAR THIS SEMESTER                          │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │ 📚 ປຶ້ມທີ່ນິຍົມທີ່ສຸດພາກຮຽນນີ້          [ເບິ່ງທັງໝົດ →]        │ │
│  │                                                              │ │
│  │  [Cover] [Cover] [Cover] [Cover] [Cover] →                │ │
│  │  Title   Title   Title   Title   Title                    │ │
│  │  Author  Author  Author  Author  Author                   │ │
│  │  ⭐4.8   ⭐4.6   ⭐4.9   ⭐4.7   ⭐4.5                      │ │
│  │                                                              │ │
│  └────────────────────────────────────────────────────────────┘ │
├──────────────────────────────────────────────────────────────────┤
│  SECTION 2: FACULTY RECOMMENDATIONS                             │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │ 🎓 ຄະນະແນະນຳໂດຍອາຈານ       [ກັ່ນຕອງຕາມຄະນະ ▼]         │ │
│  │                                                              │ │
│  │  [Cover] [Cover] [Cover] [Cover] [Cover] →                │ │
│  │  "Recommended by Prof. X, Faculty of Science"             │ │
│  │                                                              │ │
│  └────────────────────────────────────────────────────────────┘ │
├──────────────────────────────────────────────────────────────────┤
│  SECTION 3: REQUIRED FOR YOUR COURSES (Personalized)            │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │ 📋 ອ່ານບັງຄັບສຳລັບວິຊາຂອງທ່ານ                            │ │
│  │                                                              │ │
│  │  [Cover] [Cover] [Cover]                                  │ │
│  │  ACC101    ECO201    LAW301                               │ │
│  │  ບັງຄັບ  ບັງຄັບ  ບັງຄັບ                             │ │
│  │                                                              │ │
│  └────────────────────────────────────────────────────────────┘ │
├──────────────────────────────────────────────────────────────────┤
│  SECTION 4: OPEN ACCESS RESOURCES                               │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │ 🔓 ຊັບພະຍາກອນເປີດເຂົ້າເຖິງ (ຟຣີ)        [ເບິ່ງທັງໝົດ →]    │ │
│  │                                                              │ │
│  │  [Paper] [Paper] [Paper] [Paper] →                        │ │
│  │  Research papers, theses, open textbooks                  │ │
│  │                                                              │ │
│  └────────────────────────────────────────────────────────────┘ │
├──────────────────────────────────────────────────────────────────┤
│  FOOTER                                                          │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │ ກ່ຽວກັບ  |  ຊ່ວຍເຫຼືອ  |  ເງື່ອນໄຂ  |  ຄວາມເປັນສ່ວນຕົວ  |  ຕິດຕໍ່ ມຊ     │ │
│  │  © 2026 ສູນຄວາມຮູ້ລາວ - ມະຫາວິທະຍາໄລແຫ່ງຊາດລາວ   │ │
│  └────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────┘
```

---

## 6. Book Detail Page (Educational Adaptation)

### 6.1 Layout Comparison

**MEB (Commercial):**
```
┌─────────────────────────────────────────────────────┐
│  [Cover]     Title                                  │
│              Author                                 │
│              ⭐⭐⭐⭐⭐ (4.5) | 234 reviews          │
│                                                      │
│  [Read Sample]  [Add to Cart]  [Buy Now ฿150]     │
├─────────────────────────────────────────────────────┤
│  Description                                        │
│  Reviews (234)                                      │
│  Related Books                                      │
└─────────────────────────────────────────────────────┘
```

**Lao Knowledge Hub (Educational):**
```
┌─────────────────────────────────────────────────────┐
│  [Cover]     Title (ລາວ + English)                  │
│              Author: Prof. Dr. X                    │
│              Faculty of Science, NUOL               │
│              ⭐⭐⭐⭐⭐ (4.5) | 23 students used     │
│                                                      │
│  📖 Read Sample  📋 Add to List  ✅ Get Access     │
├─────────────────────────────────────────────────────┤
│  📊 Used in: ACC101, ECO201, ACC301                │
│  📑 Table of Contents                               │
│  👨‍🏫 About the Author                              │
│  💬 Student Reviews                                 │
└─────────────────────────────────────────────────────┘
```

### 6.2 Detailed Book Detail Wireframe

```
┌──────────────────────────────────────────────────────────────────┐
│  NAVIGATION                                                      │
│  ← Back to Sciences                                              │
├──────────────────────────────────────────────────────────────────┤
│  BOOK INFO                                                       │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │                                                              │ │
│  │  [Cover Image]     ພື້ນຖານການບັນຊີ                        │ │
│  │                      Fundamentals of Accounting             │ │
│  │                                                              │ │
│  │                      ຂຽນໂດຍ: ຮສ. ດຣ. ສົມສັກ ລາວວົງສີ         │ │
│  │                      Professor: Assoc. Prof. Dr. Somsak    │ │
│  │                      Faculty of Economics, NUOL            │ │
│  │                                                              │ │
│  │                      ⭐⭐⭐⭐⭐ 4.8 (23 students)           │ │
│  │                      📚 Used by 156 students this semester │ │
│  │                                                              │ │
│  │  [📖 Read Sample]  [📋 Add to List]  [✅ Get Access]       │ │
│  │                                                              │ │
│  │  💰 Price: 50,000 LAK  |  🎓 Semester Rental: 25,000 LAK  │ │
│  │                                                              │ │
│  └────────────────────────────────────────────────────────────┘ │
├──────────────────────────────────────────────────────────────────┤
│  COURSE USAGE                                                    │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │ 📊 ໃຊ້ໃນວິຊາ:                                               │ │
│  │                                                              │ │
│  │  [ACC101 - Introduction to Accounting] [Required]          │ │
│  │  [ECO201 - Microeconomics] [Recommended]                   │ │
│  │  [ACC301 - Advanced Accounting] [Required]                 │ │
│  │                                                              │ │
│  └────────────────────────────────────────────────────────────┘ │
├──────────────────────────────────────────────────────────────────┤
│  DESCRIPTION                                                     │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │ 📝 ຄຳອະທິບາຍ                                                 │ │
│  │                                                              │ │
│  │  This textbook covers fundamental accounting principles... │ │
│  │  [Read More ▼]                                             │ │
│  │                                                              │ │
│  └────────────────────────────────────────────────────────────┘ │
├──────────────────────────────────────────────────────────────────┤
│  TABLE OF CONTENTS                                               │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │ 📑 ເນື້ອໃນ                                                   │ │
│  │                                                              │ │
│  │  ▶ Chapter 1: Introduction to Accounting ......... 15 pages│ │
│  │  ▶ Chapter 2: The Accounting Equation .............. 28 pgs│ │
│  │  ▶ Chapter 3: Double-Entry System .................. 35 pgs│ │
│  │  ▶ Chapter 4: Financial Statements ................. 42 pgs│ │
│  │  ...                                                         │ │
│  │                                                              │ │
│  │  Total: 250 pages | 12 chapters                             │ │
│  └────────────────────────────────────────────────────────────┘ │
├──────────────────────────────────────────────────────────────────┤
│  ABOUT THE AUTHOR                                                │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │ 👨‍🏫 ກ່ຽວກັບຜູ້ຂຽນ                                            │ │
│  │                                                              │ │
│  │  [Photo]  Assoc. Prof. Dr. Somsak Laovongsi                │ │
│  │           Faculty of Economics, NUOL                       │ │
│  │           PhD in Accounting, Chulalongkorn University      │ │
│  │           20+ years teaching experience                    │ │
│  │           [View Profile →]                                 │ │
│  │                                                              │ │
│  └────────────────────────────────────────────────────────────┘ │
├──────────────────────────────────────────────────────────────────┤
│  STUDENT REVIEWS                                                 │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │ 💬 ຄຳເຫັນຈາກນັກຮຽນ (23)                       [Write Review] │ │
│  │                                                              │ │
│  │  ⭐⭐⭐⭐⭐                                                    │ │
│  │  "Very clear explanations, helped me pass ACC101!"         │ │
│  │  - Phone X., Economics Student                             │ │
│  │                                                              │ │
│  │  ⭐⭐⭐⭐⭐                                                     │ │
│  │  "Best accounting textbook in Lao language"                │ │
│  │  - Seng D., Accounting Major                               │ │
│  │                                                              │ │
│  │  [View All 23 Reviews →]                                   │ │
│  │                                                              │ │
│  └────────────────────────────────────────────────────────────┘ │
├──────────────────────────────────────────────────────────────────┤
│  RELATED RESOURCES                                               │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │ 📚 ຊັບພະຍາກອນທີ່ກ່ຽວຂ້ອງ                                   │ │
│  │                                                              │ │
│  │  [Book] [Book] [Book] [Book] →                            │ │
│  │  Advanced    Financial    Managerial    Audit             │ │
│  │  Accounting  Analysis   Accounting    Basics              │ │
│  │                                                              │ │
│  └────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────┘
```

---

## 7. Reader Interface (Study-Optimized)

### 7.1 Layout Comparison

**MEB (Entertainment Reading):**
```
┌─────────────────────────────────────────────────────┐
│  ← Library    Book Title           [Settings] [X]  │
├─────────────────────────────────────────────────────┤
│                                                      │
│              [PDF Page Content]                      │
│                                                      │
├─────────────────────────────────────────────────────┤
│  [◀ Prev]    Page 45 / 250    [Next ▶]             │
│                                                      │
│  [Highlight] [Note] [Bookmark] [Search]            │
└─────────────────────────────────────────────────────┘
```

**Lao Knowledge Hub (Study Reading):**
```
┌─────────────────────────────────────────────────────┐
│  ← Course    Book Title           [Tools] [Settings]│
├─────────────────────────────────────────────────────┤
│                                                      │
│              [PDF Page Content]                      │
│                                                      │
├─────────────────────────────────────────────────────┤
│  [◀ Prev]    Page 45 / 250    [Next ▶]             │
│                                                      │
│  [Highlight] [Note] [Citation] [Export] [Bookmark] │
└─────────────────────────────────────────────────────┘
```

### 7.2 Detailed Reader Wireframe

```
┌──────────────────────────────────────────────────────────────────┐
│  READER HEADER                                                   │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │ ← ACC101    ພື້ນຖານການບັນຊີ    [📚 Chapters] [⚙️ Settings] │ │
│  └────────────────────────────────────────────────────────────┘ │
├──────────────────────────────────────────────────────────────────┤
│  READING AREA                                                    │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │                                                              │ │
│  │                                                              │ │
│  │              Chapter 3: Double-Entry System                │ │
│  │                                                              │ │
│  │              The fundamental principle of accounting...     │ │
│  │              [Highlighted text in yellow]                   │ │
│  │                                                              │ │
│  │                                                              │ │
│  │  [Page 45]                                                   │ │
│  │                                                              │ │
│  └────────────────────────────────────────────────────────────┘ │
├──────────────────────────────────────────────────────────────────┤
│  READER TOOLS (Bottom Bar)                                       │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │  [◀]  Page 45 of 250  [▶]          🔖  ✏️  📑  💬  🔍      │ │
│  │                                                              │ │
│  │  Legend:  🔖 Bookmark  |  ✏️ Highlight  |  📑 Note         │ │
│  │           💬 Citation  |  🔍 Search                         │ │
│  └────────────────────────────────────────────────────────────┘ │
├──────────────────────────────────────────────────────────────────┤
│  STUDY TOOLS PANEL (Slide-up, optional)                          │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │ 📝 MY NOTES (8)          [Export to Word] [Export to PDF] │ │
│  │                                                              │ │
│  │  Page 45: "Double-entry ensures balance..." [Edit] [Delete]│ │
│  │  Page 52: "Important for exam!" [Edit] [Delete]            │ │
│  │  ...                                                         │ │
│  │                                                              │ │
│  │  📑 HIGHLIGHTS (15)                                         │ │
│  │  [Yellow: 10] [Green: 3] [Pink: 2]                         │ │
│  │                                                              │ │
│  │  🔖 BOOKMARKS (3)                                           │ │
│  │  Page 45, Page 67, Page 89                                 │ │
│  │                                                              │ │
│  └────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────┘
```

### 7.3 Study Tools Features

**New Features (vs. MEB):**

| Tool | Function | Educational Purpose |
|------|----------|---------------------|
| **Citation Generator** | Auto-generate APA/MLA/Chicago | Academic writing support |
| **Note Export** | Export notes to Word/Google Docs | Assignment preparation |
| **Highlight by Color** | Color-code by topic/importance | Study organization |
| **Chapter Navigation** | Jump to specific chapters | Quick reference |
| **Progress Tracking** | Track reading per chapter | Study planning |
| **Study Session Timer** | Track time spent reading | Study habit building |

---

## 8. Shopping/Checkout Flow (Educational)

### 8.1 Terminology Changes

| Commercial | Educational |
|------------|-------------|
| Shopping Cart | My List / Course Materials |
| Checkout | Continue / Get Access |
| Payment | Complete Access |
| Buy | Get Access |
| Purchase | Enroll / Access |
| Order | Access List |
| Receipt | Access Confirmation |

### 8.2 Checkout Flow Wireframe

```
┌──────────────────────────────────────────────────────────────────┐
│  STEP 1: MY LIST                                                 │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │ 📋 ລາຍການຂອງຂ້ອຍ                              [ຕໍ່ໄປ →]  │ │
│  │                                                              │ │
│  │  ☑  ພື້ນຖານການບັນຊີ                        50,000 LAK    │ │
│  │     Fundamentals of Accounting                              │ │
│  │     [ລຶບ]                                                │ │
│  │                                                              │ │
│  │  ☑  Microeconomics 2nd Ed                  45,000 LAK      │ │
│  │     [ລຶບ]                                                │ │
│  │                                                              │ │
│  │  ─────────────────────────────────────────                  │ │
│  │  ລວມ: 95,000 LAK                                          │ │
│  │                                                              │ │
│  │  🎓 ສ່ວນຫຼຸດນັກຮຽນ: ໃຊ້ແລ້ວ                       │ │
│  │  💡 ເຊົ່າພາກຮຽນ: ຫຼຸດ 50%                    │ │
│  │                                                              │ │
│  └────────────────────────────────────────────────────────────┘ │
├──────────────────────────────────────────────────────────────────┤
│  STEP 2: ACCESS TYPE                                             │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │ 📚 ເລືອກປະເພດການເຂົ້າເຖິງ                                   │ │
│  │                                                              │ │
│  │  ○ ເຂົ້າເຖິງເຕັມ (ຕະຫຼອດໄປ) - 95,000 LAK                      │ │
│  │    • ເຂົ້າເຖິງທຸກອຸປະກອນ                                 │ │
│  │    • ເຂົ້າເຖິງຕະຫຼອດຊີວິດ                                       │ │
│  │    • ດາວໂຫຼດອ່ານອອບໄລນໄດ້                                  │ │
│  │                                                              │ │
│  │  ● ເຊົ່າພາກຮຽນ (ແນະນຳ) - 47,500 LAK              │ │
│  │    • ເຂົ້າເຖິງຈົນຈົບພາກຮຽນ                          │ │
│  │    • ຄຸນສົມບັດຄົບຖ້ວນ                                 │ │
│  │    • ປະຢັດ 50%                                              │ │
│  │                                                              │ │
│  └────────────────────────────────────────────────────────────┘ │
├──────────────────────────────────────────────────────────────────┤
│  STEP 3: PAYMENT METHOD                                          │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │ 💳 ວິທີການຊຳລະ                                             │ │
│  │                                                              │ │
│  │  ● BCEL One                                                 │ │
│  │    ຊຳລະຜ່ານ BCEL mobile banking                             │ │
│  │                                                              │ │
│  │  ○ ໂອນຜ່ານທະນາຄານ                                            │ │
│  │    ໂອນຜ່ານ ATM ຫຼື ຄາວເຕີທະນາຄານ                        │ │
│  │                                                              │ │
│  │  ○ ບັນຊີມະຫາວິທະຍາໄລ (ຖ້າມີ)                       │ │
│  │    ຕັດຈາກບັນຊີນັກຮຽນ                               │ │
│  │                                                              │ │
│  └────────────────────────────────────────────────────────────┘ │
├──────────────────────────────────────────────────────────────────┤
│  STEP 4: CONFIRMATION                                            │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │ ✅ ຢືນຢັນການເຂົ້າເຖິງແລ້ວ                                         │ │
│  │                                                              │ │
│  │  ປຶ້ມຂອງທ່ານພ້ອມໃຊ້ງານແລ້ວ                   │ │
│  │                                                              │ │
│  │  ເລກທີ: #LKH-2026-001234                           │ │
│  │  ວັນທີ: 24 ກຸມພາ 2026                                         │ │
│  │  ຈຳນວນເງິນ: 47,500 LAK (ເຊົ່າພາກຮຽນ)                      │ │
│  │                                                              │ │
│  │  [📚 ໄປຫໍ້ສະໝຸດ]  [📧 ສົ່ງໃບເກັບເງິນທາງອີເມວ]                    │ │
│  │                                                              │ │
│  └────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────┘
```

---

## 9. Iconography

### Icon Style

**MEB:** Playful, rounded, colorful  
**Lao Knowledge Hub:** Professional, clean, academic

### Icon Set

```
Navigation Icons:
┌─────────────────────────────────────────────────────────────┐
│  🏠 Home        📚 Library      📋 Courses       👤 Profile │
│  🔍 Search      📖 Books        🎓 Faculty       ⚙️ Settings│
│  🛒 Cart        ❤️ Favorites    🔔 Notifications  🚪 Logout │
└─────────────────────────────────────────────────────────────┘

Action Icons:
┌─────────────────────────────────────────────────────────────┐
│  ➕ Add         ✏️ Edit         🗑️ Delete        📤 Export  │
│  ⬇️ Download    ⬆️ Upload       📤 Share         🔒 Access  │
│  ✓  Confirm    ✕  Cancel       ⚠️ Warning       ℹ️ Info    │
└─────────────────────────────────────────────────────────────┘

Content Icons:
┌─────────────────────────────────────────────────────────────┐
│  📖 Book        📄 Paper        🎓 Thesis        📊 Report  │
│  📝 Article     🔬 Research     📚 Textbook      📋 Syllabus│
│  👨‍🏫 Professor  🏫 University   📚 Course        🎓 Degree   │
└─────────────────────────────────────────────────────────────┘

Status Icons:
┌─────────────────────────────────────────────────────────────┐
│  ✅ Available   ⏳ Pending      ❌ Expired       🔒 Restricted│
│  🆕 New        ⭐ Featured     🔓 Open Access  📚 Required  │
│  💰 Paid      🎓 Student      👨‍🏫 Faculty       🏫 Institution│
└─────────────────────────────────────────────────────────────┘
```

---

## 10. Component Library

### 10.1 Buttons

```
Primary Button (Get Access):
┌─────────────────────────────────────────┐
│         ✅ Get Access                   │
│  Background: #1E3A8A (Deep Blue)        │
│  Text: White, 16px, Semi-Bold           │
│  Padding: 12px 24px                     │
│  Border-radius: 8px                     │
└─────────────────────────────────────────┘

Secondary Button (Read Sample):
┌─────────────────────────────────────────┐
│         📖 Read Sample                  │
│  Background: Transparent                │
│  Border: 2px solid #1E3A8A              │
│  Text: #1E3A8A, 16px, Semi-Bold         │
│  Padding: 12px 24px                     │
│  Border-radius: 8px                     │
└─────────────────────────────────────────┘

Disabled Button:
┌─────────────────────────────────────────┐
│         Get Access                      │
│  Background: #D1D5DB (Gray 300)         │
│  Text: #9CA3AF (Gray 400)               │
│  Cursor: Not-allowed                    │
└─────────────────────────────────────────┘
```

### 10.2 Book Card

```
┌─────────────────────────────────────────┐
│                                         │
│           [Cover Image]                 │
│           200x300px                     │
│                                         │
├─────────────────────────────────────────┤
│  Title (ລາວ + English)                  │
│  16px, Semi-Bold, #1F2937              │
│                                         │
│  Author                                 │
│  14px, Regular, #6B7280                │
│                                         │
│  ⭐⭐⭐⭐⭐ 4.8 (23 students)          │
│  14px, #F59E0B                         │
│                                         │
│  50,000 LAK                             │
│  16px, Bold, #1E3A8A                   │
│                                         │
│  [Required] [Semester Rental]           │
│  Badges: 12px, #059669, #F59E0B        │
└─────────────────────────────────────────┘
```

### 10.3 Badges

```
Required Badge:
┌──────────────────┐
│ 📚 Required      │
│ Background: #DCFCE7 │
│ Text: #059669, 12px, Semi-Bold │
│ Padding: 4px 8px │
│ Border-radius: 4px │
└──────────────────┘

Recommended Badge:
┌──────────────────┐
│ ⭐ Recommended   │
│ Background: #FEF3C7 │
│ Text: #D97706, 12px, Semi-Bold │
│ Padding: 4px 8px │
│ Border-radius: 4px │
└──────────────────┘

Open Access Badge:
┌──────────────────┐
│ 🔓 Open Access   │
│ Background: #DBEAFE │
│ Text: #2563EB, 12px, Semi-Bold │
│ Padding: 4px 8px │
│ Border-radius: 4px │
└──────────────────┘
```

---

## 11. Responsive Design

### Breakpoints

```
Mobile: 320px - 640px
Tablet: 641px - 1024px
Desktop: 1025px+
```

### Mobile Adaptations

**Homepage (Mobile):**
- Single column book cards
- Hamburger menu for navigation
- Collapsible sections
- Bottom navigation bar (Home, Library, Search, Profile)

**Book Detail (Mobile):**
- Cover image on top (full width)
- Stacked buttons (vertical)
- Collapsible sections (Description, TOC, Reviews)
- Sticky "Get Access" button at bottom

**Reader (Mobile):**
- Full-screen reading
- Tap to toggle toolbar
- Swipe for page navigation
- Bottom sheet for study tools

---

## 12. Accessibility

### WCAG 2.1 AA Compliance

| Requirement | Implementation |
|-------------|----------------|
| **Color Contrast** | All text meets 4.5:1 ratio minimum |
| **Font Size** | Minimum 16px, scalable to 200% |
| **Keyboard Navigation** | All actions accessible via keyboard |
| **Screen Reader** | All images have alt text |
| **Focus Indicators** | Clear focus rings on interactive elements |
| **Error Messages** | Clear, descriptive error messages |
| **Loading States** | Skeleton screens, progress indicators |

### Lao Language Support

- **Phetsarath OT** font bundled
- **Lao numerals** support (໐໑໒໓໔໕໖໗໘໙)
- **Right-to-left** compatibility (if needed)
- **Lao keyboard** support for search

---

## 13. Implementation Checklist

### Phase 1: Core UI (Weeks 1-4)

- [ ] Color palette implemented (CSS variables)
- [ ] Typography system (Phetsarath OT integration)
- [ ] Button components (Primary, Secondary, Disabled)
- [ ] Book card component
- [ ] Navigation header
- [ ] Homepage layout
- [ ] Book detail page

### Phase 2: Interactive Elements (Weeks 5-8)

- [ ] Search with filters
- [ ] Category browsing
- [ ] Shopping cart / My List
- [ ] Checkout flow
- [ ] User authentication UI

### Phase 3: Reader Interface (Weeks 9-12)

- [ ] PDF viewer integration
- [ ] Annotation tools (Highlight, Note, Bookmark)
- [ ] Study tools panel
- [ ] Citation generator
- [ ] Note export functionality

### Phase 4: Polish & Optimization (Weeks 13-16)

- [ ] Responsive design (mobile, tablet, desktop)
- [ ] Accessibility audit (WCAG 2.1 AA)
- [ ] Performance optimization
- [ ] User testing with students
- [ ] Iterate based on feedback

---

## 14. Design Assets Needed

### To Create:

1. **Logo** - Lao Knowledge Hub (incorporates NUOL elements)
2. **Icons** - Complete icon set (100+ icons)
3. **Illustrations** - Empty states, onboarding, success screens
4. **Hero Images** - Homepage hero banners
5. **Email Templates** - Transactional emails (confirmation, receipts)
6. **Social Media** - Share cards for books

### To License/Download:

1. **Phetsarath OT** font (free, open source)
2. **Icon library** (FontAwesome Pro or Heroicons)
3. **Illustration library** (unDraw or custom)

---

## 15. Next Steps

### Immediate (This Week):

1. **✅ Finalize this design spec**
2. **Create Figma mockups** - Homepage, Book Detail, Reader
3. **Design logo** - Lao Knowledge Hub + NUOL partnership
4. **Set up design system** - Colors, typography, components in Figma

### Week 3-4:

1. **User test wireframes** - 5-10 NUOL students
2. **Iterate based on feedback** - Refine UI/UX
3. **Handoff to developers** - Export assets, specs
4. **Create component library** - React/Flutter components

---

## 16. Appendix: Lao UI Translation Reference

### Common UI Elements

| English | Lao | Pronunciation |
|---------|-----|---------------|
| **Navigation** | | |
| Home | ຫຼັກ | Lak |
| Library | ຫໍ້ສະໝຸດ | Hor Sa-Mood |
| Search | ຄົ້ນຫາ | Khon Ha |
| Browse | ຊອກຫາ | Sork Ha |
| Categories | ຫຼວດໝູ່ | Mood Moo |
| All | ທັງໝົດ | Tang Mod |
| Back | ກັບຄືນ | Kub Kheun |
| Next | ຕໍ່ໄປ | Tor Pai |
| Previous | ກ່ອນໜ້າ | Korn Na |
| | **Actions** | |
| Get Access | ເຂົ້າເຖິງ | Khao Thueng |
| Read Sample | ອ່ານຕົວຢ່າງ | Aun Tua Yang |
| Add to List | ເພີ່ມໃສ່ລາຍການ | Perm Sai Lai Kan |
| Remove | ລຶບ | Loub |
| Continue | ຕໍ່ໄປ | Tor Pai |
| Confirm | ຢືນຢັນ | Yuen Yan |
| Cancel | ຍົກເລີກ | Yok Lerk |
| Save | ບັນທຶກ | Ban Thueng |
| Delete | ລຶບ | Loub |
| Edit | ແກ້ໄຂ | Kae Kai |
| Export | ສົ່ງອອກ | Song Ork |
| Download | ດາວໂຫຼດ | Dao Load |
| Upload | ອັບໂຫຼດ | Ub Load |
| | **Book Status** | |
| Required | ບັງຄັບ | Bung Kub |
| Recommended | ແນະນຳ | Na Nam |
| Available | ພ້ອມໃຊ້ງານ | Phom Sai Ngan |
| Expired | ໝົດອາຍຸ | Mod Ai |
| New | ໃໝ່ | Mai |
| Free | ຟຣີ | Free |
| | **Subjects** | |
| Sciences | ວິທະຍາສາດ | Vi Tha Ya Sat |
| Social Sciences | ວິທະຍາສາດສັງຄົມ | Vi Tha Ya Sat Sang Kom |
| Engineering | ວິສະວະກຳ | Vi Sa Va Kam |
| Law | ນິຕິສາດ | Ni Ti Sat |
| Medicine | ແພດສາດ | Phet Sat |
| Agriculture | ກະສິກຳ | Ka Si Kam |
| Education | ສຶກສາສາດ | Suek Sa Sat |
| Economics | ເສດຖະສາດ | Set Tha Sat |
| Accounting | ການບັນຊີ | Kan Ban Si |
| | **User Actions** | |
| Login | ເຂົ້າສູ່ລະບົບ | Khao Su La Bob |
| Register | ລົງທະບຽນ | Long Ta Bian |
| Logout | ອອກຈາກລະບົບ | Ork Jak La Bob |
| Profile | ໂປຣໄຟລ໌ | Profile |
| Settings | ຕັ້ງຄ່າ | Tang Kha |
| Help | ຊ່ວຍເຫຼືອ | Chuay Luea |
| | **Reading** | |
| Read | ອ່ານ | Aun |
| Page | ໜ້າ | Na |
| Chapter | ບົດ | Bod |
| Bookmark | ຄັ້ນໜ້າ | Khan Na |
| Highlight | ເນັ້ນ | Nen |
| Note | ບັນທຶກ | Ban Thueng |
| | **Payment** | |
| Price | ລາຄາ | La Kha |
| Total | ລວມ | Luam |
| Payment | ການຊຳລະ | Kan Sam La |
| Receipt | ໃບເກັບເງິນ | Boub Koub Ngern |
| Semester | ພາກຮຽນ | Pak Hian |
| Rental | ເຊົ່າ | Sao |

### Academic Phrases

| English | Lao |
|---------|-----|
| Welcome to Lao Knowledge Hub | ຍິນດີຕ້ອນຮັບສູ່ ສູນຄວາມຮູ້ລາວ |
| Access 10,000+ academic resources | ເຂົ້າເຖິງຊັບພະຍາກອນການສຶກສາກວ່າ 10,000+ |
| From National University of Laos | ຈາກ ມະຫາວິທະຍາໄລແຫ່ງຊາດລາວ |
| Most Popular This Semester | ປຶ້ມທີ່ນິຍົມທີ່ສຸດພາກຮຽນນີ້ |
| Faculty Recommendations | ຄະນະແນະນຳໂດຍອາຈານ |
| Required for Your Courses | ອ່ານບັງຄັບສຳລັບວິຊາຂອງທ່ານ |
| Open Access Resources | ຊັບພະຍາກອນເປີດເຂົ້າເຖິງ |
| Used in this course | ໃຊ້ໃນວິຊານີ້ |
| About the Author | ກ່ຽວກັບຜູ້ຂຽນ |
| Student Reviews | ຄຳເຫັນຈາກນັກຮຽນ |
| Table of Contents | ເນື້ອໃນ |
| Fundamentals of Accounting | ພື້ນຖານການບັນຊີ |
| Written by: | ຂຽນໂດຍ: |
| Professor: | ອາຈານ: |
| Faculty of Economics | ຄະນະເສດຖະສາດ |
| Used by 156 students this semester | ໃຊ້ໂດຍ 156 ນັກຮຽນໃນພາກຮຽນນີ້ |

### Numbers (Lao Numerals)

| Arabic | Lao | Name |
|--------|-----|------|
| 0 | ໐ | ສູນ |
| 1 | ໑ | ໜຶ່ງ |
| 2 | ໒ | ສອງ |
| 3 | ໓ | ສາມ |
| 4 | ໔ | ສີ່ |
| 5 | ໕ | ຫ້າ |
| 6 | ໖ | ຫົກ |
| 7 | ໗ | ເຈັດ |
| 8 | ໘ | ແປດ |
| 9 | ໙ | ກາວ |
| 10 | ໑໐ | ສິບ |
| 100 | ໑໐໐ | ໜຶ່ງຮ້ອຍ |
| 1000 | ໑໐໐໐ | ໜຶ່ງພັນ |

---

*Document Version: 1.1 | Updated: 2026-02-24 | Design Philosophy: Educational, Trustworthy, Student-Friendly | Language: Lao + English*
