from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(
    title="Lao Knowledge Hub API",
    description="Backend API for Lao Knowledge Hub digital publication platform",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict to specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Supabase
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_ANON_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "Lao Knowledge Hub API is running"}

# Specific routes MUST come before parameterized routes
@app.get("/api/v1/books/popular")
async def get_popular_books(limit: int = 10):
    """Get most popular books"""
    try:
        response = supabase.table("books").select("""
            *,
            authors (id, full_name, full_name_la)
        """).order("view_count", desc=True).limit(limit).execute()

        return {"books": response.data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/books/recommended")
async def get_recommended_books(limit: int = 10):
    """Get recommended books"""
    try:
        response = supabase.table("books").select("""
            *,
            authors (id, full_name, full_name_la)
        """).eq("is_featured", True).limit(limit).execute()

        return {"books": response.data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/books")
async def get_books(limit: int = 20, offset: int = 0):
    """Get all books with pagination"""
    try:
        response = supabase.table("books").select("""
            *,
            authors (id, full_name, full_name_la)
        """).range(offset, offset + limit - 1).execute()

        return {
            "books": response.data,
            "total": len(response.data),
            "limit": limit,
            "offset": offset
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/books/{book_id}")
async def get_book(book_id: str):
    """Get a single book by ID"""
    try:
        response = supabase.table("books").select("""
            *,
            authors (id, full_name, full_name_la)
        """).eq("id", book_id).single().execute()

        if not response.data:
            raise HTTPException(status_code=404, detail="Book not found")

        return {"book": response.data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/categories")
async def get_categories():
    """Get all categories"""
    try:
        response = supabase.table("categories").select("*").execute()
        return {"categories": response.data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/universities")
async def get_universities():
    """Get all universities"""
    try:
        response = supabase.table("universities").select("*").execute()
        return {"universities": response.data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
