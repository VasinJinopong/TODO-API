from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.core.config import settings


# Create engine
engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG
)


# Create SessionLocal
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Create Base class
Base = declarative_base()

# Dependency
def get_db():
    """Dependency สำหรับ get database session"""
    db = SessionLocal()
    try:
        yield db
        
    finally:
        db.close()
        
        