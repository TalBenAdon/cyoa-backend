from fastapi import APIRouter
from app.core.logger import get_logger
from app.core.clients import adventure_client
from app.core.clients import openrouter_client
from app.models.adventure import StartAdventure

logger = get_logger(__name__)
router = APIRouter()


@router.get("/info")
async def get_adventure_info():
    info = adventure_client.get_adventure_info()
    return info

    
#need to truely make async with httpx
@router.post("/start")
async def start_new_adventure(request : StartAdventure):
    if adventure_client.is_starting_scene():
        
  
        return await adventure_client.start_adventure(request)
        