"""ทำ database schemas"""


from sqlalchemy import Column,String, Boolean, DateTime, UniqueConstraint,Index
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid
from src.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    __table_args__ = (
        UniqueConstraint("email", name="uq_user_email"),
        UniqueConstraint("username",name="uq_user_username"),
        Index("idx_user_email", "email"),
        Index("idx_user_username","username")
    )
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    email = Column(String(255), nullable=False)
    username = Column(String(50),nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(),nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    todos = relationship("Todo",back_populates="owner", cascade="all, delete-orphan")
    def __repr__(self):
        return f"<User(id={self.id}, email={self.email}, username={self.username})>"
    
    