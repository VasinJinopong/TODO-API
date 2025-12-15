"""ทำ Database schemas สำหรับ todos"""

from sqlalchemy import Column,String, Boolean, DateTime, UniqueConstraint, Index, ForeignKey,Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid
from src.database import Base
from sqlalchemy.orm import relationship

class Todo(Base):
    __tablename__ = "todos"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4,index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text,nullable=True)
    completed = Column(Boolean, default=False, nullable=False)
    due_date = Column(DateTime(timezone=True),nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(),nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    owner_id = Column(UUID(as_uuid=True),ForeignKey("users.id", ondelete="CASCADE"),nullable=False,index=True)
    
    
    # Relationship
    owner = relationship("User",back_populates="todos")
    
    def __repr__(self):
        return f"<Todo(id={self.id}, title={self.title}, owner_id={self.owner_id})"
