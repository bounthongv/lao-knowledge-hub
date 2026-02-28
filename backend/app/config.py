from pydantic_settings import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    """Application settings loaded from environment variables"""
    
    # Supabase Configuration
    supabase_url: str
    supabase_anon_key: str
    supabase_service_key: str
    
    # JWT Settings
    jwt_secret: str = "your-super-secret-jwt-key-change-this-in-production"
    jwt_algorithm: str = "HS256"
    jwt_expiration_minutes: int = 60
    
    # BCEL Payment (optional for now)
    bcel_merchant_id: str = ""
    bcel_secret_key: str = ""
    bcel_api_url: str = "https://bcel-payment-api.com"
    
    # Application Settings
    app_name: str = "Lao Knowledge Hub API"
    debug: bool = True
    cors_origins: str = "http://localhost:3000,http://localhost:8080"
    
    # Storage
    max_file_size_mb: int = 50
    sample_pages: int = 10
    
    @property
    def cors_origins_list(self) -> List[str]:
        """Convert comma-separated CORS origins to list"""
        return [origin.strip() for origin in self.cors_origins.split(",")]
    
    @property
    def max_file_size_bytes(self) -> int:
        """Convert MB to bytes"""
        return self.max_file_size_mb * 1024 * 1024
    
    class Config:
        env_file = ".env"
        case_sensitive = True

# Global settings instance
settings = Settings()
