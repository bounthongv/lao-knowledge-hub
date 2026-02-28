-- Seed Data for Lao Knowledge Hub

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

-- Optional: Insert sample profiles (you can add these later when testing auth)
-- insert into profiles (id, full_name, email, role, university_id, faculty_id) values
-- (uuid_generate_v4(), 'John Doe', 'john@example.com', 'professor', 
--  (select id from universities where code = 'NUOL'),
--  (select id from faculties where code = 'SCI'));

-- Optional: Insert sample books (you can add these later)
-- insert into books (title_la, title_en, author_id, price_lak, status, published_at) values
-- ('ພື້ນຖານວິທະຍາສາດ', 'Fundamentals of Science', 
--  (select id from profiles where email = 'john@example.com'),
--  50000, 'published', now());

-- Note: You'll need to run this after creating the tables and RLS policies
-- Also ensure the uuid-ossp extension is enabled first