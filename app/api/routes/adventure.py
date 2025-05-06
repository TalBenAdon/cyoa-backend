from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.core.logger import get_logger
from app.core.clients import adventure_client
from app.core.clients import openrouter_client
logger = get_logger(__name__)
router = APIRouter()


@router.get("/info")
async def get_adventure_info():
    info = adventure_client.get_adventure_info()
    return info

    
#need to truely make async with httpx
@router.post("/start")
async def start_new_adventure():
    async def event_generator():
        generator = await adventure_client.start_adventure()
        async for word in generator:
            yield word        
    
            
    logger.info("/chat api route completed")
    return StreamingResponse(event_generator(), media_type="text/plain")

# @router.post("/choice")

        