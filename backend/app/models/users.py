from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime
from enum import Enum

class UserRole(str, Enum):
    """User role enum"""
    STUDENT = "student"
    PROFESSOR = "professor"
    ADMIN = "admin"

class DeviceType(str, Enum):
    """Device type enum"""
    MOBILE = "mobile"
    TABLET = "tablet"
    WEB = "web"
    DESKTOP = "desktop"

# Request Models
class UserRegister(BaseModel):
    """User registration request"""
    email: EmailStr
    password: str = Field(..., min_length=8, description="Minimum 8 characters")
    full_name: str
    phone: Optional[str] = None
    role: UserRole = UserRole.STUDENT

class UserLogin(BaseModel):
    """User login request"""
    email: EmailStr
    password: str

class DeviceRegister(BaseModel):
    """Device registration request"""
    device_fingerprint: str
    device_name: str
    device_type: DeviceType

# Response Models
class UserProfile(BaseModel):
    """User profile response"""
    id: str
    email: str
    full_name: str
    phone: Optional[str] = None
    role: UserRole
    avatar_url: Optional[str] = None
    university_id: Optional[str] = None
    faculty_id: Optional[str] = None
    is_verified: bool = False
    created_at: datetime
    
    class Config:
        from_attributes = True

class DeviceInfo(BaseModel):
    """Device information response"""
    id: str
    device_name: str
    device_type: DeviceType
    last_active_at: datetime
    created_at: datetime
