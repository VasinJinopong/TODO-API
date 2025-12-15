from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta

from src.auth import schemas
from src.auth.models import User
from src.core.security import hash_password, verify_password, create_access_token
from src.core.config import settings
from src.database import get_db

router = APIRouter(prefix="/auth", tags=["auth"])

"""
Register
Login
"""

@router.post("/register", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
async def register(user_data: schemas.UserCreate, db: Session = Depends(get_db)):
    """Register new user"""
    
    # Check email is exist
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registerd")
        
    # Check username is exist
    existing_username = db.query(User).filter(User.username == user_data.username).first()
    
    if existing_username:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already taken"
        )
        
    # Create new user
    new_user = User(
        email = user_data.email,
        username = user_data.username,
        hashed_password = hash_password(user_data.password)
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user


@router.post("/login",response_model=schemas.Token)
async def login(
    form_data : OAuth2PasswordRequestForm = Depends(), db:Session = Depends(get_db)
    ):
    """ Login user by email and password then return JWT"""
    
    user = db.query(User).filter(User.email == form_data.username).first()
    
    # Check if not exisint then raise
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect Email or Password"
        )
        
    # Verify password
    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect Email or Password"
        )
    
    # Create access token
    access_token = create_access_token(
        data={"sub": str(user.id)},expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    
    return {"access_token" : access_token, "token_type" : "bearer"}
        
    