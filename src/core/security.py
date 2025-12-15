from datetime import datetime, timedelta,timezone
from typing import Optional
from passlib.context import CryptContext
from jose import jwt
from src.core.config import settings


"""สร้างฟังก์ชั่นในการ auth ทั้งหมด"""


pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")


def hash_password(password: str) -> str:
    """Hash Password ด้วย bcrypt"""
    return pwd_context.hash(password)

def verify_password(plain_password:str , hashed_password:str) -> bool:
    """ตรวจสอบ password ว่าตรงกับ hash หรือไม่"""
    return pwd_context.verify(plain_password,hashed_password)

def create_access_token(data: dict, expires_delta:Optional[timedelta] = None) -> str:
    """สร้าง JWT Token"""
    
    to_encode = data.copy()
    
    if expires_delta:
        expires = datetime.now(timezone.utc) + expires_delta
    else:
        expires = datetime.now(timezone.utc) +timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        
    to_encode.update({"exp": expires})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    
    return encoded_jwt

def decode_access_token(token:str) -> Optional[dict]:
    """Decode JWT token"""
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except:
        return None
    
    """
    ตัวอย่าง output 
    {
        "sub" : "uuid ของ user",
        "exp" : 18582832
    }
    
    """
    