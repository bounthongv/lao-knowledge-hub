-- Sample Books Data for Lao Knowledge Hub
-- Run this in Supabase SQL Editor to add test data
-- Uses the first existing user as the author

DO $$
DECLARE
    first_user_id uuid;
BEGIN
    -- Get the first user from auth.users (or create one if none exist)
    SELECT id INTO first_user_id FROM auth.users LIMIT 1;
    
    -- If no users exist, we can't insert books (foreign key constraint)
    -- In this case, just raise a notice
    IF first_user_id IS NULL THEN
        RAISE NOTICE 'No users found in auth.users. Please register a user first via the app or Supabase Auth.';
        RAISE NOTICE 'After registering, run this script again.';
        RETURN;
    END IF;
    
    RAISE NOTICE 'Using user ID: %', first_user_id;
    
    -- Now insert sample books with this user as author
    INSERT INTO books (
        title_la, title_en, description_la, description_en, author_id, 
        price_lak, rental_price_lak, page_count, isbn, status, 
        is_featured, published_at, file_path, file_hash, 
        royalty_percentage, sample_pages, rental_period_days
    ) VALUES
    -- Computer Science
    (
        'ພື້ນຖານວິທະຍາສາດຄອມພິວເຕີ',
        'Fundamentals of Computer Science',
        'ປຶ້ມຮຽນວິທະຍາສາດຄອມພິວເຕີພື້ນຖານ ສຳລັບນັກສຶກສາປີ 1',
        'Introductory computer science textbook for first-year students covering programming basics, algorithms, and data structures.',
        first_user_id,
        45000, 22500, 320, '978-99924-1-123-456-7', 'published',
        true, now(), '/books/978-99924-1-123-456-7.pdf', 'hash_123456',
        70.00, 10, 120
    ),
    -- Lao Literature
    (
        'ວັນນະຄະດີລາວສະໄໝໃໝ່',
        'Modern Lao Literature',
        'ການສຶກສາວັນນະຄະດີລາວສະໄໝໃໝ່ ແລະ ກວີລາວ',
        'Comprehensive study of modern Lao literature, poetry, and contemporary Lao writers.',
        first_user_id,
        35000, 17500, 280, '978-99924-1-234-567-8', 'published',
        true, now(), '/books/978-99924-1-234-567-8.pdf', 'hash_234567',
        70.00, 10, 120
    ),
    -- Economics
    (
        'ຫຼັກການເສດຖະສາດຈຸລະພາກ',
        'Principles of Microeconomics',
        'ທິດສະດີເສດຖະສາດຈຸລະພາກ ແລະ ການນຳໃຊ້',
        'Microeconomic theory and applications with examples from Lao economy.',
        first_user_id,
        50000, 25000, 450, '978-99924-1-345-678-9', 'published',
        true, now(), '/books/978-99924-1-345-678-9.pdf', 'hash_345678',
        70.00, 10, 120
    ),
    -- Software Engineering
    (
        'ວິສະວະກຳໂປຣແກຣມ',
        'Software Engineering',
        'ວິຖີການພັດທະນາໂປຣແກຣມແບບມືອາຊີບ',
        'Professional software development methodologies including Agile, Scrum, and DevOps.',
        first_user_id,
        55000, 27500, 380, '978-99924-1-456-789-0', 'published',
        true, now(), '/books/978-99924-1-456-789-0.pdf', 'hash_456789',
        70.00, 10, 120
    ),
    -- Social Studies
    (
        'ສັງຄົມສາດລາວ',
        'Lao Social Studies',
        'ການສຶກສາໂຄງສ້າງສັງຄົມລາວ ແລະ ວັດທະນະທຳ',
        'Study of Lao social structure, culture, and societal changes.',
        first_user_id,
        40000, 20000, 300, '978-99924-1-567-890-1', 'published',
        true, now(), '/books/978-99924-1-567-890-1.pdf', 'hash_567890',
        70.00, 10, 120
    ),
    -- Mathematics
    (
        'ຄະນິດສາດຂັ້ນສູງ',
        'Advanced Mathematics',
        'ຄະນິດສາດຂັ້ນສູງສຳລັບນັກສຶກສາວິທະຍາສາດ',
        'Advanced mathematics for science students including calculus, linear algebra, and differential equations.',
        first_user_id,
        48000, 24000, 520, '978-99924-1-678-901-2', 'published',
        true, now(), '/books/978-99924-1-678-901-2.pdf', 'hash_678901',
        70.00, 10, 120
    ),
    -- Agriculture
    (
        'ວິທະຍາສາດກະສິກຳ',
        'Agricultural Science',
        'ເຕັກນິກການປູກຝັງ ແລະ ລ້ຽງສັດສະໄໝໃໝ່',
        'Modern farming techniques and animal husbandry for sustainable agriculture.',
        first_user_id,
        42000, 21000, 340, '978-99924-1-789-012-3', 'published',
        false, now(), '/books/978-99924-1-789-012-3.pdf', 'hash_789012',
        70.00, 10, 120
    ),
    -- Law
    (
        'ກົດໝາຍລາວ',
        'Lao Law',
        'ລະບົບກົດໝາຍແຫ່ງ ສປປ ລາວ',
        'Comprehensive overview of the Lao legal system and legislation.',
        first_user_id,
        52000, 26000, 480, '978-99924-1-890-123-4', 'published',
        false, now(), '/books/978-99924-1-890-123-4.pdf', 'hash_890123',
        70.00, 10, 120
    ),
    -- Business Administration
    (
        'ການບໍລິຫານທຸລະກິດ',
        'Business Administration',
        'ຫຼັກການບໍລິຫານທຸລະກິດສະໄໝໃໝ່',
        'Modern business administration principles with case studies from Laos.',
        first_user_id,
        47000, 23500, 360, '978-99924-1-901-234-5', 'published',
        false, now(), '/books/978-99924-1-901-234-5.pdf', 'hash_901234',
        70.00, 10, 120
    ),
    -- Education
    (
        'ພື້ນຖານການສຶກສາ',
        'Fundamentals of Education',
        'ທິດສະດີ ແລະ ວິທີການສອນສະໄໝໃໝ່',
        'Educational theory and modern teaching methodologies.',
        first_user_id,
        38000, 19000, 290, '978-99924-1-012-345-6', 'published',
        false, now(), '/books/978-99924-1-012-345-6.pdf', 'hash_012345',
        70.00, 10, 120
    );
    
    RAISE NOTICE 'Sample books inserted successfully!';
END $$;

-- Verify the data
SELECT 
    'Users' as table_name, 
    count(*) as record_count 
FROM auth.users
UNION ALL
SELECT 
    'Profiles', 
    count(*) 
FROM profiles
UNION ALL
SELECT 
    'Books', 
    count(*) 
FROM books;
