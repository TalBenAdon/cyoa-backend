from fastapi import APIRouter
from app.api.routes import ai_chat, health

api_router = APIRouter()
api_router.include_router(ai_chat.router, prefix="/ai", tags=["AI"])
api_router.include_router(health.router, prefix="", tags=["Health"])