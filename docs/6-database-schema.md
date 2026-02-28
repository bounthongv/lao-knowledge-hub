# Lao Knowledge Hub - Database Schema

**Version:** 1.0  
**Date:** 2026-02-25  
**Platform:** Supabase (PostgreSQL)

---

## Overview

This document contains the complete database schema for the Lao Knowledge Hub platform, optimized for Supabase with Row Level Security (RLS) policies.

---

## 1. Enable Required Extensions

```sql
-- Run in Supabase SQL Editor (Settings → Database → Extensions)
create extension if not exists "uuid-ossp";
create extension if not exists "pgcrypto";
```

---

## 2. Users & Authentication

Supabase Auth handles users automatically. We extend with profiles:

```sql
-- Profiles table (extends Supabase auth.users)
create table profiles (
    id uuid references auth.users on delete cascade primary key,
    full_name text not null,
    email text not null,
    phone text,
    role text default 'student' check (role in ('student', 'professor', 'admin')),
    avatar_url text,
    university_id uuid,
    faculty_id uuid,
    department text,
    is_verified boolean default false,
    created_at timestamptz default now(),
    updated_at timestamptz default now()
);

-- User devices (for DRM limiting - max 3 devices per user)
create table user_devices (
    id uuid default uuid_generate_v4() primary key,
    user_id uuid references profiles(id) on delete cascade,
    device_fingerprint text not null,
    device_name text,
    device_type text check (device_type in ('mobile', 'tablet', 'web', 'desktop')),
    last_active_at timestamptz default now(),
    created_at timestamptz default now(),
    unique(user_id, device_fingerprint)
);

-- Universities (NUOL and partner institutions)
create table universities (
    id uuid default uuid_generate_v4() primary key,
    name_la text not null,
    name_en text not null,
    code text unique not null,
    logo_url text,
    website text,
    is_active boolean default true,
    created_at timestamptz default now()
);

-- Faculties within universities
create table faculties (
    id uuid default uuid_generate_v4() primary key,
    university_id uuid references universities(id) on delete cascade,
    name_la text not null,
    name_en text not null,
    code text not null,
    dean_id uuid references profiles(id),
    is_active boolean default true,
    created_at timestamptz default now(),
    unique(university_id, code)
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

-- Anyone can view university list
alter table universities enable row level security;
create policy "Anyone can view universities"
    on universities for select
    using (true);

-- Anyone can view faculty list
alter table faculties enable row level security;
create policy "Anyone can view faculties"
    on faculties for select
    using (true);
```

---

## 3. Content Management

### 3.1 Books Table

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
    file_size bigint,
    page_count integer,
    isbn text,
    price_lak numeric(10,2) not null,
    rental_price_lak numeric(10,2),
    rental_period_days integer default 120,
    royalty_percentage numeric(5,2) default 70.00,
    status text default 'draft' check (status in ('draft', 'pending_review', 'published', 'rejected')),
    rejection_reason text,
    view_count integer default 0,
    purchase_count integer default 0,
    sample_pages integer default 10,
    is_featured boolean default false,
    published_at timestamptz,
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
    created_at timestamptz default now(),
    unique(book_id, sort_order)
);

-- Categories/Subjects
create table categories (
    id uuid default uuid_generate_v4() primary key,
    name_la text not null,
    name_en text,
    slug text unique not null,
    parent_id uuid references categories(id),
    sort_order integer default 0,
    icon_url text,
    is_active boolean default true,
    created_at timestamptz default now()
);

-- Book-Categories junction table
create table book_categories (
    book_id uuid references books(id) on delete cascade,
    category_id uuid references categories(id) on delete cascade,
    primary key (book_id, category_id)
);

-- Courses that use books
create table courses (
    id uuid default uuid_generate_v4() primary key,
    university_id uuid references universities(id) on delete cascade,
    faculty_id uuid references faculties(id) on delete cascade,
    code text not null,
    name_la text not null,
    name_en text,
    description_la text,
    description_en text,
    semester text check (semester in ('1', '2', '3', 'summer')),
    year integer,
    credits integer,
    is_active boolean default true,
    created_at timestamptz default now(),
    unique(university_id, code)
);

-- Book-Course relationships (required/recommended)
create table book_courses (
    id uuid default uuid_generate_v4() primary key,
    book_id uuid references books(id) on delete cascade,
    course_id uuid references courses(id) on delete cascade,
    relationship_type text check (relationship_type in ('required', 'recommended', 'supplementary')),
    semester_used text,
    year_used integer,
    created_at timestamptz default now(),
    unique(book_id, course_id)
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
    with check (
        auth.uid() = author_id and
        exists (select 1 from profiles where id = auth.uid() and role = 'professor')
    );

-- Authors can update their own books
create policy "Authors can update own books"
    on books for update
    using (auth.uid() = author_id);

-- Admins can view all books (via service role in API)

-- RLS for chapters
alter table chapters enable row level security;
create policy "Anyone can view chapters of published books"
    on chapters for select
    using (
        exists (select 1 from books where id = chapters.book_id and status = 'published')
    );

-- RLS for categories
alter table categories enable row level security;
create policy "Anyone can view categories"
    on categories for select
    using (true);

-- RLS for courses
alter table courses enable row level security;
create policy "Anyone can view courses"
    on courses for select
    using (is_active = true);
```

---

## 4. Purchases & Royalties

### 4.1 Orders

```sql
-- Orders
create table orders (
    id uuid default uuid_generate_v4() primary key,
    user_id uuid references profiles(id) not null,
    order_number text unique not null,
    total_amount numeric(10,2) not null,
    discount_amount numeric(10,2) default 0,
    final_amount numeric(10,2) not null,
    payment_method text check (payment_method in ('bcel_one', 'bank_transfer', 'telecom', 'credit')),
    payment_status text default 'pending' check (payment_status in ('pending', 'completed', 'failed', 'refunded')),
    bcel_transaction_id text,
    payment_metadata jsonb,
    notes text,
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
    rental_start_date date default current_date,
    rental_end_date date,
    access_expires_at timestamptz,
    is_active boolean default true,
    created_at timestamptz default now()
);

-- Royalty tracking
create table royalty_statements (
    id uuid default uuid_generate_v4() primary key,
    author_id uuid references profiles(id) not null,
    period_start date not null,
    period_end date not null,
    total_sales numeric(10,2) not null,
    platform_fee numeric(10,2) not null,
    total_royalty numeric(10,2) not null,
    status text default 'pending' check (status in ('pending', 'paid', 'cancelled')),
    paid_at timestamptz,
    payment_reference text,
    notes text,
    created_at timestamptz default now()
);

create table royalty_line_items (
    id uuid default uuid_generate_v4() primary key,
    statement_id uuid references royalty_statements(id) on delete cascade,
    book_id uuid references books(id) on delete cascade,
    order_item_id uuid references order_items(id),
    sale_amount numeric(10,2) not null,
    royalty_percentage numeric(5,2) not null,
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

-- RLS for order_items
alter table order_items enable row level security;

create policy "Users can view own order items"
    on order_items for select
    using (
        exists (select 1 from orders where id = order_items.order_id and user_id = auth.uid())
    );

-- RLS for royalty statements (authors only)
alter table royalty_statements enable row level security;

create policy "Authors can view own royalty statements"
    on royalty_statements for select
    using (auth.uid() = author_id);
```

---

## 5. Annotations & Study Tools

```sql
-- User annotations (highlights, notes, bookmarks)
create table annotations (
    id uuid default uuid_generate_v4() primary key,
    user_id uuid references profiles(id) on delete cascade,
    book_id uuid references books(id) on delete cascade,
    page_number integer not null,
    annotation_type text not null check (annotation_type in ('highlight', 'note', 'bookmark', 'drawing')),
    content text,
    color text check (color in ('yellow', 'green', 'pink', 'blue', 'orange')),
    position_data jsonb,
    tags text[],
    is_private boolean default true,
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
    total_time_minutes integer default 0,
    primary key (user_id, book_id)
);

-- Study sessions
create table study_sessions (
    id uuid default uuid_generate_v4() primary key,
    user_id uuid references profiles(id) on delete cascade,
    book_id uuid references books(id) on delete cascade,
    started_at timestamptz default now(),
    ended_at timestamptz,
    duration_minutes integer,
    pages_read integer,
    annotations_created integer,
    created_at timestamptz default now()
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

-- RLS for reading_progress
alter table reading_progress enable row level security;

create policy "Users can view own progress"
    on reading_progress for select
    using (auth.uid() = user_id);

create policy "Users can upsert own progress"
    on reading_progress for all
    using (auth.uid() = user_id)
    with check (auth.uid() = user_id);

-- RLS for study_sessions
alter table study_sessions enable row level security;

create policy "Users can view own study sessions"
    on study_sessions for select
    using (auth.uid() = user_id);

create policy "Users can create own study sessions"
    on study_sessions for insert
    with check (auth.uid() = user_id);
```

---

## 6. Reviews & Ratings

```sql
-- Book reviews
create table reviews (
    id uuid default uuid_generate_v4() primary key,
    book_id uuid references books(id) on delete cascade,
    user_id uuid references profiles(id) on delete cascade,
    rating integer not null check (rating >= 1 and rating <= 5),
    title text,
    content text not null,
    is_verified_purchase boolean default false,
    is_approved boolean default false,
    approval_reason text,
    helpful_count integer default 0,
    created_at timestamptz default now(),
    updated_at timestamptz default now(),
    unique(book_id, user_id)
);

-- Review helpfulness votes
create table review_votes (
    id uuid default uuid_generate_v4() primary key,
    review_id uuid references reviews(id) on delete cascade,
    user_id uuid references profiles(id) on delete cascade,
    is_helpful boolean not null,
    created_at timestamptz default now(),
    unique(review_id, user_id)
);

-- RLS for reviews
alter table reviews enable row level security;

create policy "Anyone can view approved reviews"
    on reviews for select
    using (is_approved = true or auth.uid() = user_id);

create policy "Users can create own reviews"
    on reviews for insert
    with check (auth.uid() = user_id);

create policy "Users can update own reviews"
    on reviews for update
    using (auth.uid() = user_id);

create policy "Users can delete own reviews"
    on reviews for delete
    using (auth.uid() = user_id);

-- RLS for review_votes
alter table review_votes enable row level security;

create policy "Users can vote on reviews"
    on review_votes for insert
    with check (auth.uid() = user_id);
```

---

## 7. Supabase Storage Buckets

```sql
-- Create storage buckets via Supabase dashboard or API:

-- 1. 'book-covers' (public)
insert into storage.buckets (id, name, public) 
values ('book-covers', 'book-covers', true);

-- 2. 'book-content' (private, signed URLs only)
insert into storage.buckets (id, name, public) 
values ('book-content', 'book-content', false);

-- 3. 'profile-avatars' (public)
insert into storage.buckets (id, name, public) 
values ('profile-avatars', 'profile-avatars', true);

-- 4. 'university-logos' (public)
insert into storage.buckets (id, name, public) 
values ('university-logos', 'university-logos', true);

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

-- Allow users to update their own covers
create policy "Users can update own covers"
    on storage.objects for update
    using (
        bucket_id = 'book-covers' and
        auth.uid()::text = (storage.foldername(name))[1]
    );

-- Only service role can access book content
-- (FastAPI backend handles signed URL generation)
create policy "Service role can manage book content"
    on storage.objects for all
    using (auth.jwt()->>'role' = 'service_role');

-- Allow users to upload avatars
create policy "Users can upload avatars"
    on storage.objects for insert
    with check (
        bucket_id = 'profile-avatars' and
        auth.uid()::text = (storage.foldername(name))[1]
    );

create policy "Anyone can view avatars"
    on storage.objects for select
    using (bucket_id = 'profile-avatars');
```

---

## 8. Database Functions & Triggers

### 8.1 Auto-create Profile on User Signup

```sql
create or replace function public.handle_new_user()
returns trigger as $$
begin
    insert into public.profiles (id, full_name, email, role)
    values (
        new.id,
        coalesce(new.raw_user_meta_data->>'full_name', split_part(new.email, '@', 1)),
        new.email,
        coalesce(new.raw_user_meta_data->>'role', 'student')
    );
    return new;
end;
$$ language plpgsql security definer;

create trigger on_auth_user_created
    after insert on auth.users
    for each row execute procedure public.handle_new_user();
```

### 8.2 Update Book View Count

```sql
create or replace function increment_view_count()
returns trigger as $$
begin
    update books set view_count = view_count + 1
    where id = new.book_id;
    return new;
end;
$$ language plpgsql;
```

### 8.3 Auto-update updated_at Timestamp

```sql
create or replace function update_updated_at_column()
returns trigger as $$
begin
    new.updated_at = now();
    return new;
end;
$$ language plpgsql;

-- Apply to all tables with updated_at
create trigger books_updated_at before update on books
    for each row execute procedure update_updated_at_column();

create trigger profiles_updated_at before update on profiles
    for each row execute procedure update_updated_at_column();

create trigger orders_updated_at before update on orders
    for each row execute procedure update_updated_at_column();

create trigger annotations_updated_at before update on annotations
    for each row execute procedure update_updated_at_column();

create trigger reviews_updated_at before update on reviews
    for each row execute procedure update_updated_at_column();
```

### 8.4 Calculate Royalty Amount

```sql
create or replace function calculate_royalty(
    p_price numeric,
    p_royalty_percentage numeric
)
returns numeric as $$
begin
    return p_price * (p_royalty_percentage / 100);
end;
$$ language plpgsql immutable;
```

### 8.5 Generate Order Number

```sql
create or replace function generate_order_number()
returns text as $$
declare
    order_num text;
begin
    select 'ORD-' || to_char(now(), 'YYYYMMDD') || '-' || lpad(nextval('orders_seq')::text, 6, '0')
    into order_num;
    return order_num;
end;
$$ language plpgsql;
```

### 8.6 Check Book Access

```sql
create or replace function check_book_access(
    p_user_id uuid,
    p_book_id uuid
)
returns boolean as $$
declare
    has_access boolean;
begin
    select exists (
        select 1 from order_items oi
        join orders o on oi.order_id = o.id
        where o.user_id = p_user_id
        and oi.book_id = p_book_id
        and oi.is_active = true
        and (oi.access_expires_at is null or oi.access_expires_at > now())
    ) into has_access;
    
    return has_access;
end;
$$ language plpgsql security definer;
```

---

## 9. Indexes for Performance

```sql
-- Books
create index idx_books_status on books(status);
create index idx_books_author on books(author_id);
create index idx_books_published_at on books(published_at desc);
create index idx_books_view_count on books(view_count desc);
create index idx_books_purchase_count on books(purchase_count desc);
create index idx_books_featured on books(is_featured) where is_featured = true;

-- Chapters
create index idx_chapters_book on chapters(book_id, sort_order);

-- Book Categories
create index idx_book_categories_book on book_categories(book_id);
create index idx_book_categories_category on book_categories(category_id);

-- Orders
create index idx_orders_user on orders(user_id);
create index idx_orders_created on orders(created_at desc);
create index idx_orders_payment_status on orders(payment_status);

-- Order Items
create index idx_order_items_order on order_items(order_id);
create index idx_order_items_book on order_items(book_id);
-- Composite index for efficient user + book lookup (used by check_book_access function)
create index idx_order_items_book_user on order_items(book_id, order_id);

-- Annotations
create index idx_annotations_user on annotations(user_id);
create index idx_annotations_book on annotations(book_id);
create index idx_annotations_type on annotations(user_id, book_id, annotation_type);

-- Reading Progress
create index idx_reading_progress_user on reading_progress(user_id);

-- Reviews
create index idx_reviews_book on reviews(book_id);
create index idx_reviews_approved on reviews(is_approved, created_at desc);
create index idx_reviews_user on reviews(user_id);

-- Courses
create index idx_courses_university on courses(university_id);
create index idx_courses_faculty on courses(faculty_id);
create index idx_courses_code on courses(code);

-- Book Courses
create index idx_book_courses_book on book_courses(book_id);
create index idx_book_courses_course on book_courses(course_id);
create index idx_book_courses_type on book_courses(relationship_type);
```

---

## 10. Seed Data

```sql
-- Insert sample universities
insert into universities (name_la, name_en, code, logo_url, website) values
('ມະຫາວິທະຍາໄລແຫ່ງຊາດລາວ', 'National University of Laos', 'NUOL', '/university-logos/nuol.png', 'https://www.nuol.edu.la'),
('ມະຫາວິທະຍາໄລຈັນກະສັດ', 'Chankaseth University', 'CSU', '/university-logos/csu.png', 'https://www.csu.edu.la');

-- Insert sample faculties for NUOL
insert into faculties (university_id, name_la, name_en, code) values
((select id from universities where code = 'NUOL'), 'ຄະນະວິທະຍາສາດ', 'Faculty of Science', 'SCI'),
((select id from universities where code = 'NUOL'), 'ຄະນະວິທະຍາສາດສັງຄົມ', 'Faculty of Social Sciences', 'SOC'),
((select id from universities where code = 'NUOL'), 'ຄະນະເສດຖະສາດ ແລະ ບໍລິຫານທຸລະກິດ', 'Faculty of Economics and Business Administration', 'ECO'),
((select id from universities where code = 'NUOL'), 'ຄະນະວິສະວະກຳສາດ', 'Faculty of Engineering', 'ENG'),
((select id from universities where code = 'NUOL'), 'ຄະນະນິຕິສາດ ແລະ ລັດຖະສາດ', 'Faculty of Law and Political Science', 'LAW');

-- Insert sample categories
insert into categories (name_la, name_en, slug, sort_order) values
('ວິທະຍາສາດ', 'Sciences', 'sciences', 1),
('ວິທະຍາສາດສັງຄົມ', 'Social Sciences', 'social-sciences', 2),
('ເສດຖະສາດ', 'Economics', 'economics', 3),
('ບໍລິຫານທຸລະກິດ', 'Business Administration', 'business', 4),
('ວິສະວະກຳສາດ', 'Engineering', 'engineering', 5),
('ນິຕິສາດ', 'Law', 'law', 6),
('ກະສິກຳສາດ', 'Agriculture', 'agriculture', 7),
('ສຶກສາສາດ', 'Education', 'education', 8),
('ແພດສາດ', 'Medicine', 'medicine', 9),
('ພາສາ ແລະ ວັດທະນະທຳ', 'Language and Culture', 'language-culture', 10);
```

---

## 11. Entity Relationship Diagram

```
┌─────────────────┐       ┌─────────────────┐
│    profiles     │       │   universities  │
├─────────────────┤       ├─────────────────┤
│ id (PK)         │       │ id (PK)         │
│ full_name       │       │ name_la         │
│ email           │       │ name_en         │
│ phone           │       │ code            │
│ role            │       │ logo_url        │
│ university_id ──┼──────▶│                 │
│ faculty_id ─────┼──────▶└─────────────────┘
└────────┬────────┘       ┌─────────────────┐
         │                │    faculties    │
         │                ├─────────────────┤
         │                │ id (PK)         │
         │                │ university_id ──┼──┐
         │                │ name_la         │  │
         │                │ name_en         │  │
         │                │ code            │  │
         │                └─────────────────┘  │
         │                                     │
         ▼                                     ▼
┌─────────────────┐       ┌─────────────────┐
│     books       │       │    courses      │
├─────────────────┤       ├─────────────────┤
│ id (PK)         │       │ id (PK)         │
│ title_la        │       │ university_id   │
│ title_en        │       │ faculty_id      │
│ author_id ──────┼──┐    │ code            │
│ cover_image_url │  │    │ name_la         │
│ file_path       │  │    │ name_en         │
│ price_lak       │  │    └────────┬────────┘
│ status          │  │             │
│ view_count      │  │             │
└────────┬────────┘  │             │
         │           │             │
         │           ▼             ▼
         │    ┌─────────────────────────┐
         │    │    book_courses         │
         │    ├─────────────────────────┤
         └───▶│ book_id (FK)            │
              │ course_id (FK)          │
              │ relationship_type       │
              └─────────────────────────┘

┌─────────────────┐       ┌─────────────────┐
│     orders      │       │   order_items   │
├─────────────────┤       ├─────────────────┤
│ id (PK)         │       │ id (PK)         │
│ user_id ────────┼──┐    │ order_id ───────┼──┐
│ order_number    │  │    │ book_id ────────┼──┐
│ total_amount    │  │    │ price           │  │
│ payment_status  │  │    │ purchase_type   │  │
└────────┬────────┘  │    │ access_expires  │  │
         │           │    └─────────────────┘  │
         │           │                         │
         ▼           ▼                         │
┌─────────────────────────┐                   │
│   royalty_statements    │                   │
├─────────────────────────┤                   │
│ id (PK)                 │                   │
│ author_id ──────────────┼───────────────────┘
│ period_start            │
│ period_end              │
│ total_royalty           │
└─────────────────────────┘

┌─────────────────┐       ┌─────────────────┐
│   annotations   │       │reading_progress │
├─────────────────┤       ├─────────────────┤
│ id (PK)         │       │ user_id (PK)    │
│ user_id         │       │ book_id (PK)    │
│ book_id         │       │ last_page       │
│ page_number     │       │ progress_%      │
│ type            │       │ total_time      │
│ content         │       └─────────────────┘
│ color           │
└─────────────────┘
```

---

## 12. Migration Scripts

### 12.1 Create All Tables (One Script)

See: `/database/migrations/001_initial_schema.sql`

### 12.2 Seed Data

See: `/database/migrations/002_seed_data.sql`

### 12.3 RLS Policies

See: `/database/migrations/003_rls_policies.sql`

---

## Next Steps

1. **Run schema in Supabase** - SQL Editor or via CLI
2. **Test RLS policies** - Verify security with different user roles
3. **Create API endpoints** - FastAPI routes to interact with schema
4. **Set up storage buckets** - Configure via Supabase dashboard
