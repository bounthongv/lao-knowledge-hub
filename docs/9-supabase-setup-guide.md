# Lao Knowledge Hub - Supabase Setup Guide

**Version:** 1.0  
**Date:** 2026-02-25  
**Purpose:** Step-by-step guide to configure Supabase after running schema

---

## Prerequisites

- ✅ Supabase project created (https://supabase.com)
- ✅ SQL schema executed successfully
- ✅ Supabase CLI installed (optional): `npm install -g supabase`

---

## Step 1: Verify Database Schema

### 1.1 Check Tables Created

Run this query in Supabase SQL Editor to verify all tables exist:

```sql
-- List all tables in public schema
SELECT table_name 
FROM information_schema.tables 
WHERE table_schema = 'public' 
  AND table_type = 'BASE TABLE'
ORDER BY table_name;
```

**Expected Result (15 tables):**
```
annotations
book_categories
book_courses
books
categories
chapters
courses
faculties
order_items
orders
profiles
reading_progress
reviews
royalty_line_items
royalty_statements
study_sessions
universities
user_devices
```

### 1.2 Check Extensions

```sql
-- Verify extensions are enabled
SELECT * FROM pg_extension WHERE extname IN ('uuid-ossp', 'pgcrypto');
```

**Expected Result:**
```
extname     | extowner | extnamespace | ...
------------+----------+--------------+...
uuid-ossp   |       10 |           10 | ...
pgcrypto    |       10 |           10 | ...
```

### 1.3 Check Functions

```sql
-- List all custom functions
SELECT routine_name, routine_type
FROM information_schema.routines
WHERE routine_schema = 'public'
  AND routine_type = 'FUNCTION'
ORDER BY routine_name;
```

**Expected Functions:**
```
calculate_royalty
check_book_access
generate_order_number
handle_new_user
increment_view_count
update_updated_at_column
```

---

## Step 2: Configure Supabase Storage

### 2.1 Create Storage Buckets

Run in SQL Editor:

```sql
-- 1. Book Covers (public)
INSERT INTO storage.buckets (id, name, public) 
VALUES ('book-covers', 'book-covers', true);

-- 2. Book Content (private)
INSERT INTO storage.buckets (id, name, public) 
VALUES ('book-content', 'book-content', false);

-- 3. Profile Avatars (public)
INSERT INTO storage.buckets (id, name, public) 
VALUES ('profile-avatars', 'profile-avatars', true);

-- 4. University Logos (public)
INSERT INTO storage.buckets (id, name, public) 
VALUES ('university-logos', 'university-logos', true);
```

### 2.2 Set Up Storage Policies

```sql
-- =====================
-- BOOK COVERS POLICIES
-- =====================

-- Allow anyone to view covers
CREATE POLICY "Anyone can view covers"
ON storage.objects FOR SELECT
USING (bucket_id = 'book-covers');

-- Allow authenticated users to upload covers
CREATE POLICY "Authenticated users can upload covers"
ON storage.objects FOR INSERT
WITH CHECK (
    bucket_id = 'book-covers' AND
    auth.role() = 'authenticated'
);

-- Allow users to update their own covers
CREATE POLICY "Users can update own covers"
ON storage.objects FOR UPDATE
USING (
    bucket_id = 'book-covers' AND
    auth.role() = 'authenticated'
);

-- Allow users to delete their own covers
CREATE POLICY "Users can delete own covers"
ON storage.objects FOR DELETE
USING (
    bucket_id = 'book-covers' AND
    auth.role() = 'authenticated'
);

-- =====================
-- BOOK CONTENT POLICIES
-- =====================

-- Only service role can access book content (backend handles signed URLs)
CREATE POLICY "Service role can manage book content"
ON storage.objects FOR ALL
USING (auth.jwt()->>'role' = 'service_role');

-- =====================
-- PROFILE AVATARS POLICIES
-- =====================

-- Allow anyone to view avatars
CREATE POLICY "Anyone can view avatars"
ON storage.objects FOR SELECT
USING (bucket_id = 'profile-avatars');

-- Allow authenticated users to upload avatars
CREATE POLICY "Users can upload avatars"
ON storage.objects FOR INSERT
WITH CHECK (
    bucket_id = 'profile-avatars' AND
    auth.role() = 'authenticated'
);

-- Allow users to update their own avatars
CREATE POLICY "Users can update own avatars"
ON storage.objects FOR UPDATE
USING (
    bucket_id = 'profile-avatars' AND
    auth.role() = 'authenticated'
);

-- =====================
-- UNIVERSITY LOGOS POLICIES
-- =====================

-- Allow anyone to view university logos
CREATE POLICY "Anyone can view university logos"
ON storage.objects FOR SELECT
USING (bucket_id = 'university-logos');

-- Only admins can upload logos
CREATE POLICY "Admins can upload university logos"
ON storage.objects FOR INSERT
WITH CHECK (
    bucket_id = 'university-logos' AND
    auth.jwt()->>'role' = 'service_role'
);
```

### 2.3 Verify Storage Buckets

Go to **Storage** in Supabase Dashboard → You should see:
- ✅ book-covers (Public)
- ✅ book-content (Private)
- ✅ profile-avatars (Public)
- ✅ university-logos (Public)

---

## Step 3: Insert Seed Data

### 3.1 Insert Universities

```sql
INSERT INTO universities (name_la, name_en, code, logo_url, website) VALUES
('ມະຫາວິທະຍາໄລແຫ່ງຊາດລາວ', 'National University of Laos', 'NUOL', '/university-logos/nuol.png', 'https://www.nuol.edu.la'),
('ມະຫາວິທະຍາໄລຈັນກະສັດ', 'Chankaseth University', 'CSU', '/university-logos/csu.png', 'https://www.csu.edu.la'),
('ມະຫາວິທະຍາໄລຈຳປາສັກ', 'Champasak University', 'CPU', '/university-logos/cpu.png', 'https://www.cpu.edu.la');
```

### 3.2 Insert Faculties for NUOL

```sql
INSERT INTO faculties (university_id, name_la, name_en, code) VALUES
((SELECT id FROM universities WHERE code = 'NUOL'), 'ຄະນະວິທະຍາສາດ', 'Faculty of Science', 'SCI'),
((SELECT id FROM universities WHERE code = 'NUOL'), 'ຄະນະວິທະຍາສາດສັງຄົມ', 'Faculty of Social Sciences', 'SOC'),
((SELECT id FROM universities WHERE code = 'NUOL'), 'ຄະນະເສດຖະສາດ ແລະ ບໍລິຫານທຸລະກິດ', 'Faculty of Economics and Business Administration', 'ECO'),
((SELECT id FROM universities WHERE code = 'NUOL'), 'ຄະນະວິສະວະກຳສາດ', 'Faculty of Engineering', 'ENG'),
((SELECT id FROM universities WHERE code = 'NUOL'), 'ຄະນະນິຕິສາດ ແລະ ລັດຖະສາດ', 'Faculty of Law and Political Science', 'LAW'),
((SELECT id FROM universities WHERE code = 'NUOL'), 'ຄະນະກະສິກຳສາດ', 'Faculty of Agriculture', 'AGR'),
((SELECT id FROM universities WHERE code = 'NUOL'), 'ຄະນະສຶກສາສາດ', 'Faculty of Education', 'EDU'),
((SELECT id FROM universities WHERE code = 'NUOL'), 'ຄະນະແພດສາດ', 'Faculty of Medicine', 'MED');
```

### 3.3 Insert Categories

```sql
INSERT INTO categories (name_la, name_en, slug, sort_order) VALUES
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

### 3.4 Insert Sample Courses

```sql
INSERT INTO courses (university_id, faculty_id, code, name_la, name_en, semester, year, credits) VALUES
-- Economics Faculty Courses
((SELECT id FROM universities WHERE code = 'NUOL'), 
 (SELECT id FROM faculties WHERE code = 'ECO' AND university_id = (SELECT id FROM universities WHERE code = 'NUOL')),
 'ACC101', 'ບົດນຳການບັນຊີ', 'Introduction to Accounting', '1', 1, 3),
 
((SELECT id FROM universities WHERE code = 'NUOL'), 
 (SELECT id FROM faculties WHERE code = 'ECO' AND university_id = (SELECT id FROM universities WHERE code = 'NUOL')),
 'ECO201', 'ເສດຖະສາດຈຸລະພາກ', 'Microeconomics', '2', 2, 3),
 
((SELECT id FROM universities WHERE code = 'NUOL'), 
 (SELECT id FROM faculties WHERE code = 'ECO' AND university_id = (SELECT id FROM universities WHERE code = 'NUOL')),
 'ACC301', 'ການບັນຊີຂັ້ນສູງ', 'Advanced Accounting', '1', 3, 3),

-- Science Faculty Courses
((SELECT id FROM universities WHERE code = 'NUOL'), 
 (SELECT id FROM faculties WHERE code = 'SCI' AND university_id = (SELECT id FROM universities WHERE code = 'NUOL')),
 'MATH101', 'ຄະນິດສາດພື້ນຖານ', 'Fundamental Mathematics', '1', 1, 4),
 
((SELECT id FROM universities WHERE code = 'NUOL'), 
 (SELECT id FROM faculties WHERE code = 'SCI' AND university_id = (SELECT id FROM universities WHERE code = 'NUOL')),
 'PHYS101', 'ຟີຊິກພື້ນຖານ', 'Fundamental Physics', '1', 1, 4);
```

### 3.5 Verify Seed Data

```sql
-- Count records in each table
SELECT 'universities' as table_name, COUNT(*) as count FROM universities
UNION ALL
SELECT 'faculties', COUNT(*) FROM faculties
UNION ALL
SELECT 'categories', COUNT(*) FROM categories
UNION ALL
SELECT 'courses', COUNT(*) FROM courses;
```

**Expected Result:**
```
table_name   | count
-------------+-------
universities |     3
faculties    |     8
categories   |    10
courses      |     5
```

---

## Step 4: Test RLS Policies

### 4.1 Create Test Users

First, get your Supabase URL and anon key from **Settings → API**:

```bash
# You'll need these for testing
SUPABASE_URL="https://your-project.supabase.co"
SUPABASE_ANON_KEY="your-anon-key"
```

### 4.2 Test RLS: Profiles Table

```sql
-- Test 1: Anonymous user cannot view profiles (should return 0 rows)
-- Run this without being logged in
SELECT COUNT(*) FROM profiles;
-- Expected: ERROR (RLS policy blocks access)

-- Test 2: User can view own profile (after login)
-- This will work after authentication
SELECT id, email, full_name FROM profiles WHERE id = auth.uid();
```

### 4.3 Test RLS: Books Table

```sql
-- Test 1: Anyone can view published books
SELECT id, title_la FROM books WHERE status = 'published';
-- Expected: List of published books (or empty if none)

-- Test 2: Draft books are not visible
SELECT id, title_la FROM books WHERE status = 'draft';
-- Expected: ERROR or empty (RLS blocks access)

-- Test 3: Only professors can insert books
-- This requires authenticated user with role='professor'
```

### 4.4 Test RLS: Orders Table

```sql
-- Test 1: Users can only view own orders
SELECT id, order_number FROM orders WHERE user_id = auth.uid();
-- Expected: Only current user's orders

-- Test 2: Users cannot view other users' orders
-- Try to query with a different user_id
SELECT id, order_number FROM orders WHERE user_id = 'other-user-uuid';
-- Expected: ERROR (RLS policy violation)
```

### 4.5 Test Using Supabase Dashboard

1. Go to **Authentication → Users**
2. Create a test user manually
3. Use **SQL Editor** with "Run as role" dropdown to test different roles:
   - `postgres` (admin)
   - `authenticated` (logged-in user)
   - `anon` (anonymous user)
   - `service_role` (backend)

---

## Step 5: Get API Credentials

### 5.1 Find Your Credentials

Go to **Settings → API** in Supabase Dashboard:

```
Project URL: https://xxxxxxxxxxxxx.supabase.co
anon/public key: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
service_role key: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9... (SECRET!)
```

### 5.2 Create .env File

Create a `.env` file in your project root:

```bash
# Supabase Configuration
SUPABASE_URL="https://xxxxxxxxxxxxx.supabase.co"
SUPABASE_ANON_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
SUPABASE_SERVICE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." (keep secret!)

# Database
DATABASE_URL="postgresql://postgres:[YOUR-PASSWORD]@db.xxxxxxxxxxxxx.supabase.co:5432/postgres"

# BCEL Payment (will get later)
BCEL_MERCHANT_ID=""
BCEL_SECRET_KEY=""

# JWT Secret (for FastAPI)
JWT_SECRET="your-random-secret-key-here"
```

⚠️ **Important:** Add `.env` to `.gitignore` to avoid committing secrets!

---

## Step 6: Test Database Connection

### 6.1 Using Supabase SQL Editor

Go to **SQL Editor** and run:

```sql
-- Test all functions
SELECT calculate_royalty(50000, 70);
-- Expected: 35000

SELECT generate_order_number();
-- Expected: ORD-20260225-000001 (or similar)

-- Test check_book_access (will return false since no orders yet)
SELECT check_book_access(
    '00000000-0000-0000-0000-000000000000',
    '00000000-0000-0000-0000-000000000000'
);
-- Expected: false
```

### 6.2 Using psql (Optional)

```bash
# Connect to your Supabase database
psql postgresql://postgres:[YOUR-PASSWORD]@db.xxxxxxxxxxxxx.supabase.co:5432/postgres

# Test connection
\dt  -- List all tables
\df  -- List all functions
```

---

## Step 7: Configure Auth Settings

### 7.1 Enable Email Auth

Go to **Authentication → Providers → Email**:

- ✅ Enable Email Provider
- ✅ Enable Confirm Email (recommended)
- ✅ Enable Double Opt-in (recommended for production)

### 7.2 Configure Email Templates

Go to **Authentication → Email Templates**:

**Verify email template:**
```
Subject: Confirm your email - Lao Knowledge Hub

Hi {{ .UserEmail }},

Welcome to Lao Knowledge Hub! Please confirm your email address by clicking the link below:

{{ .ConfirmationURL }}

Thank you,
Lao Knowledge Hub Team
```

### 7.3 Set Site URL

Go to **Authentication → URL Configuration**:

- **Site URL:** `https://laoknowledgehub.la` (or your Firebase URL)
- **Redirect URLs:** 
  - `http://localhost:3000` (development)
  - `http://localhost:8080` (Flutter dev)
  - `https://laoknowledgehub.la/*`

---

## Step 8: Verify Everything Works

### 8.1 Final Checklist

```sql
-- Run this comprehensive check query
SELECT 
    (SELECT COUNT(*) FROM universities) as universities_count,
    (SELECT COUNT(*) FROM faculties) as faculties_count,
    (SELECT COUNT(*) FROM categories) as categories_count,
    (SELECT COUNT(*) FROM courses) as courses_count,
    (SELECT COUNT(*) FROM storage.buckets) as storage_buckets_count,
    (SELECT COUNT(*) FROM pg_extension WHERE extname IN ('uuid-ossp', 'pgcrypto')) as extensions_count;
```

**Expected Result:**
```
universities | faculties | categories | courses | storage_buckets | extensions
-------------+-----------+------------+---------+-----------------+------------
           3 |         8 |         10 |       5 |               4 |          2
```

### 8.2 Test User Registration Flow

1. Go to your app's registration page (or use Supabase Auth UI)
2. Create a test user
3. Verify email confirmation
4. Check `profiles` table for auto-created profile

### 8.3 Test Storage Upload

In Supabase Dashboard → **Storage**:

1. Select `book-covers` bucket
2. Upload a test image
3. Verify it's publicly accessible
4. Copy the public URL

---

## Troubleshooting

### Issue: RLS Policy Error

```
ERROR: new row violates row-level security policy
```

**Solution:** Check which policy is blocking. Run as `postgres` role to debug:

```sql
-- View all policies for a table
SELECT schemaname, tablename, policyname, permissive, roles, cmd, qual, with_check
FROM pg_policies
WHERE tablename = 'books';
```

### Issue: Function Not Found

```
ERROR: function check_book_access(uuid,uuid) does not exist
```

**Solution:** Re-run the function creation SQL. Check schema:

```sql
SELECT routine_name, routine_schema 
FROM information_schema.routines 
WHERE routine_name = 'check_book_access';
```

### Issue: Storage Bucket Not Accessible

```
ERROR: permission denied for table objects
```

**Solution:** Verify bucket exists and policies are set:

```sql
SELECT id, name, public FROM storage.buckets;

-- Check policies
SELECT * FROM storage.policies WHERE bucket_id = 'book-covers';
```

### Issue: Trigger Not Working

```
ERROR: profile not created on user signup
```

**Solution:** Verify trigger exists:

```sql
SELECT tgname, tgrelid::regclass, tgfoid::regprocedure
FROM pg_trigger
WHERE tgname = 'on_auth_user_created';
```

Re-create trigger if needed:

```sql
DROP TRIGGER IF EXISTS on_auth_user_created ON auth.users;

CREATE TRIGGER on_auth_user_created
    AFTER INSERT ON auth.users
    FOR EACH ROW EXECUTE PROCEDURE public.handle_new_user();
```

---

## Next Steps

✅ **Supabase Setup Complete!**

Now proceed to:

1. **Set up FastAPI Backend** → See `docs/9-fastapi-setup-guide.md`
2. **Set up Flutter App** → See `docs/10-flutter-setup-guide.md`
3. **Configure BCEL Payment** → Contact BCEL for API credentials

---

## Quick Reference

### Supabase Dashboard URLs

- **Project Dashboard:** `https://app.supabase.com/project/YOUR-PROJECT`
- **SQL Editor:** `https://app.supabase.com/project/YOUR-PROJECT/sql`
- **Authentication:** `https://app.supabase.com/project/YOUR-PROJECT/auth/users`
- **Storage:** `https://app.supabase.com/project/YOUR-PROJECT/storage`
- **API Settings:** `https://app.supabase.com/project/YOUR-PROJECT/settings/api`

### Important Commands

```sql
-- Reset sequences (if needed)
SELECT setval('orders_seq', (SELECT MAX(id) FROM orders));

-- View all RLS policies
SELECT schemaname, tablename, policyname, cmd, qual 
FROM pg_policies 
WHERE schemaname = 'public';

-- View storage usage
SELECT 
    bucket_id,
    COUNT(*) as file_count,
    SUM(metadata->>'size')::bigint as total_bytes
FROM storage.objects
GROUP BY bucket_id;
```
