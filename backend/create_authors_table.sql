-- Create independent authors table (not linked to auth.users)
-- This allows any book to be added without requiring the author to have an account

-- Create authors table
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

-- Add index for faster lookups
CREATE INDEX IF NOT EXISTS idx_authors_name ON authors(full_name);

-- Add comment
COMMENT ON TABLE authors IS 'Independent authors table - authors do not need user accounts';

-- Grant permissions
ALTER TABLE authors ENABLE ROW LEVEL SECURITY;

-- Anyone can read authors
CREATE POLICY "Anyone can view authors"
    ON authors FOR SELECT
    USING (true);

-- Only admins can modify (you can add admin check later)
CREATE POLICY "Admins can manage authors"
    ON authors FOR ALL
    USING (true); -- Temporarily allow all for testing

-- Now update books table to reference authors instead of profiles
-- First, check if we need to add author_id column or if it already exists
