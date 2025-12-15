from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.core.config import settings
from src.database import Base,engine
from src.auth.router import router as auth_router
from src.todos.router import router as todos_router
from src.exceptions.handlers import global_exception_handler, http_exception_handler


# Create tables
Base.metadata.create_all(bind=engine)

# Create app
app = FastAPI(
    title= settings.PROJECT_NAME,
    version="1.0.0",
    description="TODO API with FastAPI"
)

# Exception handlers
app.add_exception_handler(Exception,global_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials = True,
    allow_methods= ["*"],
    allow_headers=["*"]
    
)


# Health check
@app.get("/health")
def health_check():
    return {"status": "ok", "version" : "1.0.0"}

# Include router
app.include_router(auth_router, prefix=settings.API_V1_STR)
app.include_router(todos_router,prefix=settings.API_V1_STR)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "src.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG
    )