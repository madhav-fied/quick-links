from fastapi import APIRouter
from backend.api.routes import redirect

api_v1_router = APIRouter()

api_v1_router.include_router(
    redirect.router, 
    prefix="/rdr", 
    tags=["Quick Redirection"]
)
