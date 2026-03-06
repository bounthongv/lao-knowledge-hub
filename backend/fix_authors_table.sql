-- Quick Fix: Create authors table and update books relationship
-- Run this in Supabase SQL Editor

-- 1. Create authors table
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

-- 2. Create index
CREATE INDEX IF NOT EXISTS idx_authors_name ON authors(full_name);

-- 3. Enable RLS
ALTER TABLE authors ENABLE ROW LEVEL SECURITY;

-- 4. Create policies (allow public read for now)
DROP POLICY IF EXISTS "Anyone can view authors" ON authors;
CREATE POLICY "Anyone can view authors"
    ON authors FOR SELECT
    USING (true);

DROP POLICY IF EXISTS "Admins can manage authors" ON authors;
CREATE POLICY "Admins can manage authors"
    ON authors FOR ALL
    USING (true);

-- 5. Fix books foreign key (if needed)
-- First check if books.author_id references profiles or authors
DO $$
BEGIN
    -- Drop old constraint if it references profiles
    ALTER TABLE books DROP CONSTRAINT IF EXISTS books_author_id_fkey;
    
    -- Add new constraint to authors
    ALTER TABLE books
        ADD CONSTRAINT books_author_id_fkey
        FOREIGN KEY (author_id)
        REFERENCES authors(id);
EXCEPTION
    WHEN OTHERS THEN
        RAISE NOTICE 'Foreign key already correct or error: %', SQLERRM;
END $$;

-- 6. Verify
SELECT 'Authors table created successfully!' as status;
