from pydantic import BaseModel,Field
from datetime import datetime
from uuid import UUID
from typing import Optional


class TodoBase(BaseModel):
    """Base schema สำหรับ Todo"""
    title: str = Field(min_length=1, max_length=255)
    description: Optional[str] = None
    completed: bool = False
    due_date: Optional[datetime] = None
    
    
class TodoCreate(TodoBase):
    """schema สำหรับสร้าง todo (ไม่ค้องส่ง completed)"""
    pass    
    
    
    
class TodoUpdate(TodoBase):
    """Schema สำหรับ update TODO (ทุกอย้่าง)"""
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = None
    completed: Optional[bool] = None
    due_date: Optional[datetime] = None
    
    
class TodoResponse(TodoBase):
    """Schema สำหรับ response"""
    id : UUID
    owner_id : UUID
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True
    
    