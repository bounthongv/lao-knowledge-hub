"""
Seed script to populate Supabase with sample data for testing.
Run this after the database schema is set up.
"""
import os
from supabase import create_client, Client
from dotenv import load_dotenv
from datetime import datetime
import uuid

# Load environment variables
load_dotenv()

# Initialize Supabase client
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY")

if not SUPABASE_URL or not SUPABASE_SERVICE_KEY:
    raise ValueError("Missing Supabase credentials. Check your .env file.")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)

print("✅ Connected to Supabase")

# Sample data
UNIVERSITIES = [
    {"name_la": "ມະຫາວິທະຍາໄລແຫ່ງຊາດລາວ", "name_en": "National University of Laos", "code": "NUOL", "logo_url": "/university-logos/nuol.png", "website": "https://www.nuol.edu.la"},
    {"name_la": "ມະຫາວິທະຍາໄລຈັນກະສັດ", "name_en": "Chankaseth University", "code": "CSU", "logo_url": "/university-logos/csu.png", "website": "https://www.csu.edu.la"},
    {"name_la": "ມະຫາວິທະຍາໄລຈຳປາສັກ", "name_en": "Champasak University", "code": "CPU", "logo_url": "/university-logos/cpu.png", "website": "https://www.cpu.edu.la"},
]

FACULTIES = [
    {"university_code": "NUOL", "name_la": "ຄະນະວິທະຍາສາດ", "name_en": "Faculty of Science", "code": "SCI"},
    {"university_code": "NUOL", "name_la": "ຄະນະວິທະຍາສາດສັງຄົມ", "name_en": "Faculty of Social Sciences", "code": "SOC"},
    {"university_code": "NUOL", "name_la": "ຄະນະເສດຖະສາດ ແລະ ບໍລິຫານທຸລະກິດ", "name_en": "Faculty of Economics and Business Administration", "code": "ECO"},
    {"university_code": "NUOL", "name_la": "ຄະນະວິສະວະກຳສາດ", "name_en": "Faculty of Engineering", "code": "ENG"},
    {"university_code": "NUOL", "name_la": "ຄະນະນິຕິສາດ ແລະ ລັດຖະສາດ", "name_en": "Faculty of Law and Political Science", "code": "LAW"},
    {"university_code": "NUOL", "name_la": "ຄະນະສຶກສາສາດ", "name_en": "Faculty of Education", "code": "EDU"},
    {"university_code": "NUOL", "name_la": "ຄະນະກະສິກຳສາດ", "name_en": "Faculty of Agriculture", "code": "AGR"},
    {"university_code": "CSU", "name_la": "ຄະນະເຕັກໂນໂລຊີຂໍ້ມູນຂ່າວສານ", "name_en": "Faculty of Information Technology", "code": "FIT"},
    {"university_code": "CSU", "name_la": "ຄະນະພາສາຕ່າງປະເທດ", "name_en": "Faculty of Foreign Languages", "code": "FFL"},
]

CATEGORIES = [
    {"name_la": "ວິທະຍາສາດ", "name_en": "Sciences", "slug": "sciences", "sort_order": 1},
    {"name_la": "ວິທະຍາສາດສັງຄົມ", "name_en": "Social Sciences", "slug": "social-sciences", "sort_order": 2},
    {"name_la": "ເສດຖະສາດ", "name_en": "Economics", "slug": "economics", "sort_order": 3},
    {"name_la": "ບໍລິຫານທຸລະກິດ", "name_en": "Business Administration", "slug": "business", "sort_order": 4},
    {"name_la": "ວິສະວະກຳສາດ", "name_en": "Engineering", "slug": "engineering", "sort_order": 5},
    {"name_la": "ນິຕິສາດ", "name_en": "Law", "slug": "law", "sort_order": 6},
    {"name_la": "ກະສິກຳສາດ", "name_en": "Agriculture", "slug": "agriculture", "sort_order": 7},
    {"name_la": "ສຶກສາສາດ", "name_en": "Education", "slug": "education", "sort_order": 8},
    {"name_la": "ແພດສາດ", "name_en": "Medicine", "slug": "medicine", "sort_order": 9},
    {"name_la": "ພາສາ ແລະ ວັດທະນະທຳ", "name_en": "Language and Culture", "slug": "language-culture", "sort_order": 10},
    {"name_la": "ເຕັກໂນໂລຊີຂໍ້ມູນຂ່າວສານ", "name_en": "Information Technology", "slug": "it", "sort_order": 11},
    {"name_la": "ຄະນິດສາດ", "name_en": "Mathematics", "slug": "mathematics", "sort_order": 12},
]

# Sample professor profiles (these would normally be created via auth)
PROFILES = [
    {"full_name": "Dr. Somchai Vongphachan", "full_name_la": "ດຣ. ສົມໄຊ ວົງພະຈັນ", "email": "somchai.v@nuol.edu.la", "role": "professor"},
    {"full_name": "Dr. Vilay Phonephakdy", "full_name_la": "ດຣ. ວິໄລ ໂພນະພັກດີ", "email": "vilay.p@nuol.edu.la", "role": "professor"},
    {"full_name": "Prof. Bounmy Sisavath", "full_name_la": "ຜສ. ບຸນມີ ສີສະວາດ", "email": "bounmy.s@nuol.edu.la", "role": "professor"},
    {"full_name": "Dr. Khamsing Keomanivong", "full_name_la": "ດຣ. ຄຳສິງ ແກ້ວມະນີວົງ", "email": "khamsing.k@nuol.edu.la", "role": "professor"},
    {"full_name": "Prof. Phetdavanh Souvannalath", "full_name_la": "ຜສ. ເພັດດາວັນ ສຸວັນນະລາດ", "email": "phetdavanh.s@nuol.edu.la", "role": "professor"},
    {"full_name": "Dr. Sysavath Intharath", "full_name_la": "ດຣ. ສີສະວາດ ອິນທະຣາດ", "email": "sysavath.i@nuol.edu.la", "role": "professor"},
    {"full_name": "Prof. Latsamy Phonevilay", "full_name_la": "ຜສ. ລັດສະໝີ ໂພນະວິໄລ", "email": "latsamy.p@nuol.edu.la", "role": "professor"},
    {"full_name": "Dr. Anousone Tampasack", "full_name_la": "ດຣ. ອານຸສອນ ຕຳປາສັກ", "email": "anousone.t@nuol.edu.la", "role": "professor"},
]

BOOKS = [
    {
        "title_la": "ພື້ນຖານວິທະຍາສາດຄອມພິວເຕີ",
        "title_en": "Fundamentals of Computer Science",
        "author_email": "somchai.v@nuol.edu.la",
        "category_slug": "it",
        "description_la": "ປຶ້ມຮຽນວິທະຍາສາດຄອມພິວເຕີພື້ນຖານ ສຳລັບນັກສຶກສາປີ 1",
        "description_en": "Introductory computer science textbook for first-year students covering programming basics, algorithms, and data structures.",
        "price_lak": 45000,
        "page_count": 320,
        "isbn": "978-99924-1-123-456-7",
        "edition": "1st Edition",
        "published_year": 2024,
        "is_featured": True,
        "cover_color": "#3B82F6"
    },
    {
        "title_la": "ວັນນະຄະດີລາວສະໄໝໃໝ່",
        "title_en": "Modern Lao Literature",
        "author_email": "vilay.p@nuol.edu.la",
        "category_slug": "language-culture",
        "description_la": "ການສຶກສາວັນນະຄະດີລາວສະໄໝໃໝ່ ແລະ ກວີລາວ",
        "description_en": "Comprehensive study of modern Lao literature, poetry, and contemporary Lao writers.",
        "price_lak": 35000,
        "page_count": 280,
        "isbn": "978-99924-1-234-567-8",
        "edition": "2nd Edition",
        "published_year": 2023,
        "is_featured": True,
        "cover_color": "#10B981"
    },
    {
        "title_la": "ຫຼັກການເສດຖະສາດຈຸລະພາກ",
        "title_en": "Principles of Microeconomics",
        "author_email": "bounmy.s@nuol.edu.la",
        "category_slug": "economics",
        "description_la": "ທິດສະດີເສດຖະສາດຈຸລະພາກ ແລະ ການນຳໃຊ້",
        "description_en": "Microeconomic theory and applications with examples from Lao economy.",
        "price_lak": 50000,
        "page_count": 450,
        "isbn": "978-99924-1-345-678-9",
        "edition": "3rd Edition",
        "published_year": 2024,
        "is_featured": True,
        "cover_color": "#F59E0B"
    },
    {
        "title_la": "ວິສະວະກຳໂປຣແກຣມ",
        "title_en": "Software Engineering",
        "author_email": "khamsing.k@nuol.edu.la",
        "category_slug": "engineering",
        "description_la": "ວິຖີການພັດທະນາໂປຣແກຣມແບບມືອາຊີບ",
        "description_en": "Professional software development methodologies including Agile, Scrum, and DevOps.",
        "price_lak": 55000,
        "page_count": 380,
        "isbn": "978-99924-1-456-789-0",
        "edition": "1st Edition",
        "published_year": 2025,
        "is_featured": True,
        "cover_color": "#8B5CF6"
    },
    {
        "title_la": "ສັງຄົມສາດລາວ",
        "title_en": "Lao Social Studies",
        "author_email": "phetdavanh.s@nuol.edu.la",
        "category_slug": "social-sciences",
        "description_la": "ການສຶກສາໂຄງສ້າງສັງຄົມລາວ ແລະ ວັດທະນະທຳ",
        "description_en": "Study of Lao social structure, culture, and societal changes.",
        "price_lak": 40000,
        "page_count": 300,
        "isbn": "978-99924-1-567-890-1",
        "edition": "2nd Edition",
        "published_year": 2023,
        "is_featured": True,
        "cover_color": "#EC4899"
    },
    {
        "title_la": "ຄະນິດສາດຂັ້ນສູງ",
        "title_en": "Advanced Mathematics",
        "author_email": "sysavath.i@nuol.edu.la",
        "category_slug": "mathematics",
        "description_la": "ຄະນິດສາດຂັ້ນສູງສຳລັບນັກສຶກສາວິທະຍາສາດ",
        "description_en": "Advanced mathematics for science students including calculus, linear algebra, and differential equations.",
        "price_lak": 48000,
        "page_count": 520,
        "isbn": "978-99924-1-678-901-2",
        "edition": "4th Edition",
        "published_year": 2024,
        "is_featured": True,
        "cover_color": "#EF4444"
    },
    {
        "title_la": "ວິທະຍາສາດກະສິກຳ",
        "title_en": "Agricultural Science",
        "author_email": "latsamy.p@nuol.edu.la",
        "category_slug": "agriculture",
        "description_la": "ເຕັກນິກການປູກຝັງ ແລະ ລ້ຽງສັດສະໄໝໃໝ່",
        "description_en": "Modern farming techniques and animal husbandry for sustainable agriculture.",
        "price_lak": 42000,
        "page_count": 340,
        "isbn": "978-99924-1-789-012-3",
        "edition": "1st Edition",
        "published_year": 2024,
        "is_featured": False,
        "cover_color": "#84CC16"
    },
    {
        "title_la": "ກົດໝາຍລາວ",
        "title_en": "Lao Law",
        "author_email": "anousone.t@nuol.edu.la",
        "category_slug": "law",
        "description_la": "ລະບົບກົດໝາຍແຫ່ງ ສປປ ລາວ",
        "description_en": "Comprehensive overview of the Lao legal system and legislation.",
        "price_lak": 52000,
        "page_count": 480,
        "isbn": "978-99924-1-890-123-4",
        "edition": "2nd Edition",
        "published_year": 2023,
        "is_featured": False,
        "cover_color": "#6366F1"
    },
    {
        "title_la": "ການບໍລິຫານທຸລະກິດ",
        "title_en": "Business Administration",
        "author_email": "bounmy.s@nuol.edu.la",
        "category_slug": "business",
        "description_la": "ຫຼັກການບໍລິຫານທຸລະກິດສະໄໝໃໝ່",
        "description_en": "Modern business administration principles with case studies from Laos.",
        "price_lak": 47000,
        "page_count": 360,
        "isbn": "978-99924-1-901-234-5",
        "edition": "1st Edition",
        "published_year": 2025,
        "is_featured": False,
        "cover_color": "#14B8A6"
    },
    {
        "title_la": "ພື້ນຖານການສຶກສາ",
        "title_en": "Fundamentals of Education",
        "author_email": "phetdavanh.s@nuol.edu.la",
        "category_slug": "education",
        "description_la": "ທິດສະດີ ແລະ ວິທີການສອນສະໄໝໃໝ່",
        "description_en": "Educational theory and modern teaching methodologies.",
        "price_lak": 38000,
        "page_count": 290,
        "isbn": "978-99924-1-012-345-6",
        "edition": "3rd Edition",
        "published_year": 2024,
        "is_featured": False,
        "cover_color": "#F97316"
    },
]

def seed_universities():
    """Insert sample universities"""
    print("\n📚 Seeding universities...")
    for uni in UNIVERSITIES:
        try:
            data, count = supabase.table("universities").insert(uni).execute()
            print(f"  ✅ Added: {uni['name_en']}")
        except Exception as e:
            if "duplicate" in str(e).lower() or "unique" in str(e).lower():
                print(f"  ⚠️  Already exists: {uni['name_en']}")
            else:
                print(f"  ❌ Error adding {uni['name_en']}: {e}")

def seed_faculties():
    """Insert sample faculties"""
    print("\n🏛️  Seeding faculties...")
    # Get university IDs
    unis = supabase.table("universities").select("id, code").execute()
    uni_map = {u["code"]: u["id"] for u in unis.data}
    
    for fac in FACULTIES:
        if fac["university_code"] in uni_map:
            try:
                data = {
                    "university_id": uni_map[fac["university_code"]],
                    "name_la": fac["name_la"],
                    "name_en": fac["name_en"],
                    "code": fac["code"]
                }
                result = supabase.table("faculties").insert(data).execute()
                print(f"  ✅ Added: {fac['name_en']}")
            except Exception as e:
                if "duplicate" in str(e).lower() or "unique" in str(e).lower():
                    print(f"  ⚠️  Already exists: {fac['name_en']}")
                else:
                    print(f"  ❌ Error adding {fac['name_en']}: {e}")

def seed_categories():
    """Insert sample categories"""
    print("\n📑 Seeding categories...")
    for cat in CATEGORIES:
        try:
            data, count = supabase.table("categories").insert(cat).execute()
            print(f"  ✅ Added: {cat['name_en']}")
        except Exception as e:
            if "duplicate" in str(e).lower() or "unique" in str(e).lower():
                print(f"  ⚠️  Already exists: {cat['name_en']}")
            else:
                print(f"  ❌ Error adding {cat['name_en']}: {e}")

def seed_books():
    """Insert sample books"""
    print("\n📖 Seeding books...")
    
    # Since we can't create profiles without auth users, we'll use a workaround:
    # Insert books with a placeholder author_id (we'll use the admin user if exists, or skip)
    # For testing, let's query existing profiles first
    
    profiles = supabase.table("profiles").select("id, email").execute()
    profile_map = {p["email"]: p["id"] for p in profiles.data} if profiles.data else {}
    
    # Get category IDs
    categories = supabase.table("categories").select("id, slug").execute()
    category_map = {c["slug"]: c["id"] for c in categories.data}
    
    for book in BOOKS:
        try:
            # Check if book already exists
            existing = supabase.table("books").select("id").eq("isbn", book["isbn"]).execute()
            if existing.data:
                print(f"  ⚠️  Already exists: {book['title_en']}")
                continue
            
            # Try to find author profile
            author_id = profile_map.get(book["author_email"])
            category_id = category_map.get(book["category_slug"])
            
            if not author_id:
                # Skip books without authors for now
                print(f"  ⚠️  Skipping (no author profile): {book['title_en']}")
                continue
            
            if not category_id:
                print(f"  ⚠️  Category not found: {book['category_slug']}")
                continue
            
            data = {
                "title_la": book["title_la"],
                "title_en": book["title_en"],
                "author_id": author_id,
                "description_la": book["description_la"],
                "description_en": book["description_en"],
                "price_lak": book["price_lak"],
                "page_count": book["page_count"],
                "isbn": book["isbn"],
                "is_featured": book["is_featured"],
                "status": "published",
                "published_at": datetime.now().isoformat(),
                "file_path": f"/books/{book['isbn']}.pdf",
                "file_hash": f"hash_{book['isbn']}",
                "rental_price_lak": book["price_lak"] * 0.5,
                "rental_period_days": 120,
                "royalty_percentage": 70.00,
                "sample_pages": 10,
            }
            
            result = supabase.table("books").insert(data).execute()
            print(f"  ✅ Added: {book['title_en']}")
        except Exception as e:
            print(f"  ❌ Error adding {book['title_en']}: {e}")

def main():
    """Run all seed functions"""
    print("=" * 60)
    print("🚀 Lao Knowledge Hub - Database Seeder")
    print("=" * 60)
    
    seed_universities()
    seed_faculties()
    seed_categories()
    # Skip profiles - they need to be created via auth
    seed_books()
    
    print("\n" + "=" * 60)
    print("✅ Seeding complete!")
    print("=" * 60)
    
    # Show summary
    print("\n📊 Summary:")
    try:
        unis = supabase.table("universities").select("id", count="exact").execute()
        print(f"  • Universities: {unis.count}")
        
        facs = supabase.table("faculties").select("id", count="exact").execute()
        print(f"  • Faculties: {facs.count}")
        
        cats = supabase.table("categories").select("id", count="exact").execute()
        print(f"  • Categories: {cats.count}")
        
        books = supabase.table("books").select("id", count="exact").execute()
        print(f"  • Books: {books.count}")
    except Exception as e:
        print(f"  ⚠️  Could not fetch summary: {e}")
    
    print("\n💡 Note: Books require author profiles. Create a test user via the app first!")

if __name__ == "__main__":
    main()
