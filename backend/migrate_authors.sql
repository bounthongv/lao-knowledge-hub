-- Migration: Change books.author_id from profiles to independent authors table
-- This allows books to exist without requiring authors to have user accounts

-- Step 1: Create authors table (if not exists)
CREATE TABLE IF NOT EXISTS authors (
    id uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
    full_name text NOT NULL,
    full_name_la text,
    biography text,
    biography_la text,
    email text,
    website text,
    is_active boolean DEFAULT true,
    created_at timestamptz DEFAULT now(),
    updated_at timestamptz DEFAULT now()
);

-- Step 2: Drop the foreign key constraint on books.author_id
-- (We'll keep the column but make it reference authors instead)
ALTER TABLE books DROP CONSTRAINT IF EXISTS books_author_id_fkey;

-- Step 3: Add new foreign key to authors table
ALTER TABLE books 
    ADD CONSTRAINT books_author_id_fkey 
    FOREIGN KEY (author_id) 
    REFERENCES authors(id);

-- Step 4: Enable RLS on authors
ALTER TABLE authors ENABLE ROW LEVEL SECURITY;

-- Step 5: Create policies
-- Anyone can read authors
DROP POLICY IF EXISTS "Anyone can view authors" ON authors;
CREATE POLICY "Anyone can view authors"
    ON authors FOR SELECT
    USING (true);

-- Admins can manage authors (simplified - allow all for now)
DROP POLICY IF EXISTS "Admins can manage authors" ON authors;
CREATE POLICY "Admins can manage authors"
    ON authors FOR ALL
    USING (true);

-- Step 6: Add indexes for performance
CREATE INDEX IF NOT EXISTS idx_authors_name ON authors(full_name);
CREATE INDEX IF NOT EXISTS idx_books_author ON books(author_id);

-- Done! Now you can:
-- 1. Create authors independently
-- 2. Assign books to any author
-- 3. Authors don't need user accounts
