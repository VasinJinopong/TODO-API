from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from src.core.config import logger
import traceback


async def global_exception_handler(request: Request, exc:Exception):
    """Handle all unhandler exceptions"""
    logger.error(
        "unhandler_excrption",
        path=str(request.url.path),
        method = request.method,
        error= str(exc),
        traceback = traceback.format_exc()
    )
    
    return JSONResponse(
        status_code=500,
        content={
            "error": "internal_server_error",
            "message": "An unexpected error occured"
        }
    )
    
    
async def http_exception_handler(request: Request, exc: Exception):
    """Handle HTTP exceptions"""
    logger.warning(
        "http_exception",
        status_code = exc.status_code,
        detail=exc.detail,
        path=str(request.url.path),
        method=request.method
    )
    
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error" : exc.status_code,
            "message": exc.detail
        }
    )