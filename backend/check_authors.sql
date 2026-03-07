-- Check if authors table has data and books can join
-- Run this in Supabase SQL Editor

-- 1. Check authors table
SELECT 'Authors count:' as info, count(*) as count FROM authors;

-- 2. Check a sample author
SELECT id, full_name, full_name_la FROM authors LIMIT 3;

-- 3. Check if books can join with authors
SELECT 
    b.title_en,
    b.author_id,
    a.full_name
FROM books b
LEFT JOIN authors a ON b.author_id = a.id
LIMIT 5;

-- 4. Check foreign key constraint
SELECT 
    tc.constraint_name, 
    tc.table_name, 
    kcu.column_name, 
    ccu.table_name AS foreign_table_name,
    ccu.column_name AS foreign_column_name 
FROM information_schema.table_constraints AS tc 
JOIN information_schema.key_column_usage AS kcu
    ON tc.constraint_name = kcu.constraint_name
JOIN information_schema.constraint_column_usage AS ccu
    ON ccu.constraint_name = tc.constraint_name
WHERE tc.constraint_name = 'books_author_id_fkey';
