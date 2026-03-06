# Adding Sample Data for Testing

This guide explains how to add sample book data to your Supabase database for testing the Flutter app.

---

## Option 1: Run SQL Script in Supabase Dashboard (Recommended)

### Steps:

1. **Open Supabase Dashboard**
   - Go to: https://app.supabase.com
   - Select your project: `nbvyybvgcdfeazcvecvy`

2. **Open SQL Editor**
   - Click on **SQL Editor** in the left sidebar
   - Click **New Query**

3. **Copy and Run the SQL Script**
   - Open the file: `backend/seed_books_direct.sql`
   - Copy the entire contents
   - Paste into the SQL Editor
   - Click **Run** (or press Ctrl+Enter)

4. **Verify the Data**
   - You should see a result showing counts for all tables
   - Expected: 10 books, 8 professor profiles

5. **Test the API**
   ```bash
   # Start the backend if not already running
   cd backend
   D:\lao-knowledge-hub\backend\venv\Scripts\python.exe -m uvicorn app.main:app --reload --port 8000
   
   # Test in browser or curl
   curl http://localhost:8000/api/v1/books
   curl http://localhost:8000/api/v1/books/popular
   curl http://localhost:8000/api/v1/books/recommended
   ```

---

## Option 2: Create Test User via App First

If you prefer to create books linked to real user accounts:

### Steps:

1. **Start the Backend**
   ```bash
   cd backend
   D:\lao-knowledge-hub\backend\venv\Scripts\python.exe -m uvicorn app.main:app --reload --port 8000
   ```

2. **Start the Flutter App**
   ```bash
   cd flutter-app
   flutter run -d chrome
   ```

3. **Register a Test User**
   - Go to the app
   - Click "Login" → "Register"
   - Create an account with email: `test.prof@nuol.edu.la`
   - Complete email verification if required

4. **Update User Role to Professor**
   - Go to Supabase Dashboard
   - Open **Table Editor** → **profiles**
   - Find your test user
   - Edit the `role` field from `student` to `professor`
   - Save

5. **Manually Add Books**
   - Use Supabase Table Editor → **books**
   - Click "Insert" → Add new row
   - Fill in the required fields:
     - `title_la`: ພື້ນຖານວິທະຍາສາດຄອມພິວເຕີ
     - `title_en`: Fundamentals of Computer Science
     - `author_id`: Select your profile UUID
     - `price_lak`: 45000
     - `status`: published
     - `file_path`: /books/test-book.pdf
     - `file_hash`: hash_test123
     - `is_featured`: true
     - `published_at`: [current date]

---

## Sample Book Data

The SQL script (`seed_books_direct.sql`) includes these 10 sample books:

| # | Title (EN) | Title (LA) | Price (LAK) | Featured |
|---|------------|------------|-------------|----------|
| 1 | Fundamentals of Computer Science | ພື້ນຖານວິທະຍາສາດຄອມພິວເຕີ | 45,000 | ✅ |
| 2 | Modern Lao Literature | ວັນນະຄະດີລາວສະໄໝໃໝ່ | 35,000 | ✅ |
| 3 | Principles of Microeconomics | ຫຼັກການເສດຖະສາດຈຸລະພາກ | 50,000 | ✅ |
| 4 | Software Engineering | ວິສະວະກຳໂປຣແກຣມ | 55,000 | ✅ |
| 5 | Lao Social Studies | ສັງຄົມສາດລາວ | 40,000 | ✅ |
| 6 | Advanced Mathematics | ຄະນິດສາດຂັ້ນສູງ | 48,000 | ✅ |
| 7 | Agricultural Science | ວິທະຍາສາດກະສິກຳ | 42,000 | ❌ |
| 8 | Lao Law | ກົດໝາຍລາວ | 52,000 | ❌ |
| 9 | Business Administration | ການບໍລິຫານທຸລະກິດ | 47,000 | ❌ |
| 10 | Fundamentals of Education | ພື້ນຖານການສຶກສາ | 38,000 | ❌ |

---

## Testing the Complete Flow

After adding sample data:

1. **Start Backend** (if not running):
   ```bash
   cd D:\lao-knowledge-hub\backend
   D:\lao-knowledge-hub\backend\venv\Scripts\python.exe -m uvicorn app.main:app --reload --port 8000
   ```

2. **Start Flutter App**:
   ```bash
   cd D:\lao-knowledge-hub\flutter-app
   flutter run -d chrome
   ```

3. **Test the Flow**:
   - Landing page should display
   - Click "Get Started" → Login
   - Register/Login with any account
   - Home screen should now show:
     - **Most Popular** section (6 books sorted by view_count)
     - **Recommended** section (6 featured books)
   - Each book card shows:
     - Cover color placeholder
     - Title in Lao/English
     - Author name
     - Price in LAK

4. **Verify API Endpoints**:
   - Visit http://localhost:8000/docs
   - Test `/api/v1/books/popular`
   - Test `/api/v1/books/recommended`
   - Check response includes book data

---

## Troubleshooting

### "No books yet" message still showing

1. **Check if books exist in database**:
   - Go to Supabase Dashboard
   - Table Editor → books
   - Verify books are present

2. **Check backend logs**:
   - Look for errors in the terminal running uvicorn
   - Check for CORS or connection errors

3. **Test API directly**:
   ```bash
   curl http://localhost:8000/api/v1/books/popular
   ```
   Should return JSON with books array

### API returns error about "profiles" table

Make sure the database schema is fully set up:
- Run the complete schema from `docs/6-database-schema.md`
- Or use Supabase SQL Editor to create missing tables

### Books show but authors are null

The `author_id` must reference a valid profile in the `profiles` table. The SQL script creates sample professor profiles automatically.

---

## Next Steps

After verifying books display correctly:

1. **Add Book Detail Screen** - Click on book to see full details
2. **Implement Search** - Search by title, author, category
3. **Add Book Upload** - Admin interface to add new books
4. **Implement Cart & Checkout** - Purchase flow
5. **Add PDF Reader** - Read purchased books

---

## Files Reference

- `backend/seed_books_direct.sql` - SQL script to add sample data
- `backend/seed_database.py` - Python seed script (requires existing profiles)
- `backend/app/main.py` - FastAPI endpoints
- `flutter-app/lib/screens/home/home_screen.dart` - Home screen displaying books

---

**Last Updated:** 2026-03-06
