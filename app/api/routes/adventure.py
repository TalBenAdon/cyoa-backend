from fastapi import APIRouter
from app.core.logger import get_logger
from app.core.clients import adventure_client
logger = get_logger(__name__)
router = APIRouter()


@router.get("/info")
async def get_adventure_info():
    info = adventure_client.get_adventure_info()
    if info:
        return info
    

@router.post("/start")
async def start_new_adventure():
    