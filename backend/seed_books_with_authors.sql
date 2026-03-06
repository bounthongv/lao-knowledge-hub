-- Sample Data for Lao Knowledge Hub
-- Run this in Supabase SQL Editor
-- Authors are now independent (don't need user accounts)

-- Step 1: Create sample authors
INSERT INTO authors (full_name, full_name_la, biography, biography_la, email) VALUES
('Dr. Somchai Vongphachan', 'ດຣ. ສົມໄຊ ວົງພະຈັນ', 'Professor of Computer Science at NUOL', 'ສາດສະດາຈານ ຄອມພິວເຕີ ມະຫາວິທະຍາໄລແຫ່ງຊາດລາວ', 'somchai.v@nuol.edu.la'),
('Dr. Vilay Phonephakdy', 'ດຣ. ວິໄລ ໂພນະພັກດີ', 'Expert in Lao Language and Literature', 'ຜູ້ຊ່ຽວຊານ ພາສາ ແລະ ວັນນະຄະດີລາວ', 'vilay.p@nuol.edu.la'),
('Prof. Bounmy Sisavath', 'ຜສ. ບຸນມີ ສີສະວາດ', 'Economics and Business Administration', 'ເສດຖະສາດ ແລະ ບໍລິຫານທຸລະກິດ', 'bounmy.s@nuol.edu.la'),
('Dr. Khamsing Keomanivong', 'ດຣ. ຄຳສິງ ແກ້ວມະນີວົງ', 'Engineering and Technology', 'ວິສະວະກຳ ແລະ ເຕັກໂນໂລຊີ', 'khamsing.k@nuol.edu.la'),
('Prof. Phetdavanh Souvannalath', 'ຜສ. ເພັດດາວັນ ສຸວັນນະລາດ', 'Social Sciences Research', 'ການວິໄຈວິທະຍາສາດສັງຄົມ', 'phetdavanh.s@nuol.edu.la'),
('Dr. Sysavath Intharath', 'ດຣ. ສີສະວາດ ອິນທະຣາດ', 'Mathematics and Statistics', 'ຄະນິດສາດ ແລະ ສະຖິຕິ', 'sysavath.i@nuol.edu.la'),
('Prof. Latsamy Phonevilay', 'ຜສ. ລັດສະໝີ ໂພນະວິໄລ', 'Agriculture and Environmental Science', 'ກະສິກຳ ແລະ ວິທະຍາສາດສິ່ງແວດລ້ອມ', 'latsamy.p@nuol.edu.la'),
('Dr. Anousone Tampasack', 'ດຣ. ອານຸສອນ ຕຳປາສັກ', 'Law and Political Science', 'ນິຕິສາດ ແລະ ລັດຖະສາດ', 'anousone.t@nuol.edu.la');

-- Step 2: Get author IDs for use in books
DO $$
DECLARE
    author1_id uuid;
    author2_id uuid;
    author3_id uuid;
    author4_id uuid;
    author5_id uuid;
    author6_id uuid;
    author7_id uuid;
    author8_id uuid;
BEGIN
    -- Get author IDs by email
    SELECT id INTO author1_id FROM authors WHERE email = 'somchai.v@nuol.edu.la';
    SELECT id INTO author2_id FROM authors WHERE email = 'vilay.p@nuol.edu.la';
    SELECT id INTO author3_id FROM authors WHERE email = 'bounmy.s@nuol.edu.la';
    SELECT id INTO author4_id FROM authors WHERE email = 'khamsing.k@nuol.edu.la';
    SELECT id INTO author5_id FROM authors WHERE email = 'phetdavanh.s@nuol.edu.la';
    SELECT id INTO author6_id FROM authors WHERE email = 'sysavath.i@nuol.edu.la';
    SELECT id INTO author7_id FROM authors WHERE email = 'latsamy.p@nuol.edu.la';
    SELECT id INTO author8_id FROM authors WHERE email = 'anousone.t@nuol.edu.la';
    
    -- Step 3: Insert sample books
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
        author1_id,
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
        author2_id,
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
        author3_id,
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
        author4_id,
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
        author5_id,
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
        author6_id,
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
        author7_id,
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
        author8_id,
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
        author3_id,
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
        author5_id,
        38000, 19000, 290, '978-99924-1-012-345-6', 'published',
        false, now(), '/books/978-99924-1-012-345-6.pdf', 'hash_012345',
        70.00, 10, 120
    );
    
    RAISE NOTICE 'Sample data inserted: 8 authors and 10 books created successfully!';
END $$;

-- Verify the data
SELECT 
    'Authors' as table_name, 
    count(*) as record_count 
FROM authors
UNION ALL
SELECT 
    'Books', 
    count(*) 
FROM books;
