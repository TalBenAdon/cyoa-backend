from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.core.logger import get_logger
from app.core.clients import adventure_client
from app.models.adventure import AdvanceAdventure, StartAdventure
logger = get_logger(__name__)
router = APIRouter()


@router.get("/info")
async def get_adventure_info():
    info = adventure_client.get_adventure_info()
    return info

    

@router.post("/start")
async def start_new_adventure(request: StartAdventure):
    if adventure_client.is_starting_scene():
        async def event_generator():
            generator = await adventure_client.start_adventure(request.type)
            async for word in generator:
                yield word        
        
                
        logger.info("/start adventure route completed")
        return StreamingResponse(event_generator(), media_type="text/plain")



@router.post("/choice")
async def advance_adventure(request : AdvanceAdventure):
    if not adventure_client.is_starting_scene():
        async def event_generator():
            generator = await adventure_client.advance_scene(request.choice)
            async for word in generator:
                yield word        
        
                
        logger.info("/choice adventure route completed")
        return StreamingResponse(event_generator(), media_type="text/plain")

        