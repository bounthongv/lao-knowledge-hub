import time

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routes import annotations, auth, books, payments, progress

# Create FastAPI app
app = FastAPI(
    title=settings.app_name,
    description="API for Lao Knowledge Hub - Digital Publication Platform for Laos",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS Middleware - allows requests from Flutter web and Next.js
# Note: allow_credentials must be False if using wildcard '*' in origins
cors_origins = settings.cors_origins_list
allow_credentials = True
if "*" in cors_origins:
    allow_credentials = False

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=allow_credentials,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])
app.include_router(books.router, prefix="/api/v1/books", tags=["Books"])
app.include_router(payments.router, prefix="/api/v1/payments", tags=["Payments"])
app.include_router(annotations.router, prefix="/api/v1", tags=["Annotations"])
app.include_router(
    progress.router, prefix="/api/v1/progress", tags=["Reading Progress"]
)


# Health check endpoint
@app.get("/health")
def health_check():
    """Check API health status"""
    return {
        "status": "healthy",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "version": "1.0.0",
    }


# Root endpoint
@app.get("/")
def root():
    """Welcome message"""
    return {
        "message": "Welcome to Lao Knowledge Hub API",
        "docs": "/docs",
        "health": "/health",
        "github": "https://github.com/your-org/lao-knowledge-hub",
    }


# Startup event
@app.on_event("startup")
async def startup_event():
    """Run on application startup"""
    print(f"🚀 Starting {settings.app_name}...")
    print(f"📚 API Documentation: http://localhost:8000/docs")
    print(f"❤️  Health Check: http://localhost:8000/health")
    print(f"🔗 Supabase URL: {settings.supabase_url}")


# Shutdown event
@app.on_event("shutdown")
async def shutdown_event():
    """Run on application shutdown"""
    print("👋 Shutting down...")
