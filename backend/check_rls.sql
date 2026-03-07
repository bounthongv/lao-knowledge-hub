-- Test authors RLS policies
-- Run this in Supabase SQL Editor

-- Check current RLS policies on authors
SELECT 
    schemaname,
    tablename,
    policyname,
    permissive,
    roles,
    cmd,
    qual,
    with_check
FROM pg_policies
WHERE tablename = 'authors';

-- Check if books can select authors
SELECT 
    b.title_en,
    b.author_id,
    a.full_name,
    a.full_name_la
FROM books b
LEFT JOIN authors a ON b.author_id = a.id
LIMIT 3;
