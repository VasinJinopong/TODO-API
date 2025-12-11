from pydantic_settings import BaseSettings



"""Pydantic model สำหรับดึงค่าจาก .env"""

class Settings(BaseSettings):
    
    # DATABASE
    DATABASE_URL: str
    
    # JWT
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # API
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "TODO API"
    DEBUG: bool = True
    
    #CORS
    CORS_ORIGINS: list[str] = ["*"]
    
    class Config:
        env_file = ".env"
        
settings = Settings()