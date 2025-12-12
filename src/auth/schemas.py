"""ทำ pydantic model"""

from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from uuid import UUID


class UserBase(BaseModel):
    """Base schema สำหรับ User"""
    email: EmailStr
    username: str = Field(min_length=3, max_length=50)
    
    
class UserCreate(UserBase):
    """Schema สำหรับ register user"""
    password: str = Field(min_length=8, max_length=100)
    
    
class UserLogin(BaseModel):
    """Schema สำหรับ Login"""
    email: EmailStr
    password: str
    
    
class UserResponse(UserBase):
    """Schema สำหรับ response แบบไม่มี password"""
    id: UUID
    created_at: datetime
    
    class Config:
        from_attributes : True
        
        
class Token(BaseModel):
    """Schema สำหรับ JWT token"""
    access_token: str
    token_type: str = "bearer"