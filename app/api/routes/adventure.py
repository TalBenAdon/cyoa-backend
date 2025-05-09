from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.core.logger import get_logger
from app.models.adventure import AdvanceAdventure, StartAdventure
from app.exceptions.HasExistingAdventureException import HasExistingAdventureException
from app.exceptions.AdventureNotFound import AdventureNotFound
from app.services.adventure_manager import create_adventure, get_adventure
logger = get_logger(__name__)
router = APIRouter()





@router.get("/info/{adventure_id}")
async def get_adventure_info(adventure_id):
    adventure = get_adventure(adventure_id)
    if not adventure:
        logger.warning("Adventure was not found when asked for info")
        raise AdventureNotFound()
    return adventure.get_adventure_info()

    

@router.post("/start")
async def start_new_adventure(request: StartAdventure):
    adventure = create_adventure(request.type)
    if adventure.is_starting_scene():
        
        async def event_generator():
            generator = await adventure.start_adventure()
            async for word in generator:
                yield word        
        
                
        logger.info("/start adventure route completed")
        return StreamingResponse(event_generator(), media_type="text/plain", headers={"X-Adventure-ID": adventure.id})
    else:
        logger.warning("User already has an adventure")
        raise HasExistingAdventureException()



@router.post("/choice/{adventure_id}")
async def advance_adventure(request : AdvanceAdventure):
    adventure = get_adventure(request.adventure_id)
    if not adventure.is_starting_scene():
        async def event_generator():
            generator = await adventure.advance_scene(request.choice)
            async for word in generator:
                yield word        
        
                
        logger.info("/choice adventure route completed")
        return StreamingResponse(event_generator(), media_type="text/plain")

        