# Lao Knowledge Hub - Backend Setup

## Quick Start

### 1. Create Virtual Environment

```bash
cd backend

# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

```bash
# Copy example env file
copy .env.example .env  # Windows
# or
cp .env.example .env    # macOS/Linux
```

Edit `.env` and add your Supabase credentials:

```env
SUPABASE_URL="https://your-project.supabase.co"
SUPABASE_ANON_KEY="your-anon-key"
SUPABASE_SERVICE_KEY="your-service-role-key"
```

### 4. Run Development Server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 5. Test API

Open your browser:
- **API Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health
- **Root**: http://localhost:8000/

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI app
│   ├── config.py         # Configuration
│   ├── database.py       # Supabase client
│   ├── models/           # Pydantic models
│   ├── routes/           # API endpoints
│   └── middleware/       # Auth middleware
├── tests/
├── .env
├── .env.example
├── requirements.txt
└── README.md
```

## API Endpoints

Once running, visit http://localhost:8000/docs for interactive API documentation.

### Available Endpoints:

- `GET /health` - Health check
- `GET /api/v1/books` - List books
- `GET /api/v1/books/{id}` - Get book details
- `GET /api/v1/books/{id}/sample` - Get sample pages
- `POST /api/v1/auth/me` - Get current user

## Troubleshooting

### Module not found
Make sure virtual environment is activated and you're in the `backend` directory.

### Supabase connection error
Check your `.env` file has correct Supabase URL and keys.

### Port already in use
Change port: `uvicorn app.main:app --reload --port 8001`
