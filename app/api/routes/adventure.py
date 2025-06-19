from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.utils.get_system_message import get_system_message
from app.core.logger import get_logger
from app.core.database.db_helpers import save_adventure
from app.models.adventure import AdvanceAdventure, StartAdventure, AdventureInfoResponse, AdventuresIdListResponse
from app.exceptions.HasExistingAdventureException import HasExistingAdventureException
from app.exceptions.AdventureNotFound import AdventureNotFound
from app.services.adventure_manager import (create_adventure,
                                            get_adventure_with_history_snapshot,
                                            get_adventures,
                                            get_adventure)

logger = get_logger(__name__)
router = APIRouter()

@router.get("/adventures", response_model=AdventuresIdListResponse)
async def return_adventures_ids():
    return AdventuresIdListResponse(adventures=get_adventures())



@router.get("/info/{adventure_id}", response_model=AdventureInfoResponse)
async def get_adventure_info(adventure_id):
    adventure = get_adventure_with_history_snapshot(adventure_id)
    if not adventure:
        logger.warning("Adventure was not found when asked for info")
        raise AdventureNotFound()
    
    return AdventureInfoResponse(
        id=adventure.id,
        type=adventure.type,
        scene_number=adventure.scene_number,
        history=adventure.history,
    )

    

@router.post(
        "/start", 
        responses={
            200: {
                "content":{"text/plain":{}},
                "description": "Returns a streamed an adventure start narration with options"
            }})
async def start_new_adventure(request: StartAdventure):
    adventure = create_adventure(request.type)
    system_message = get_system_message(request.type)
        
    async def event_generator():
        generator = await adventure.start_adventure(system_message)
        async for word in generator:
            yield word        
        
        save_adventure(adventure)
        
        logger.info("/start adventure route completed streaming")
    
    return StreamingResponse(event_generator(), media_type="text/plain", headers={"X-Adventure-ID": adventure.id})




@router.post("/choice/{adventure_id}", 
        responses={
            200: {
                "content":{"text/plain":{}},
                "description": "Returns a streamed adventure narration with options corresponding to the last chosen option"
            }})
async def advance_adventure(adventure_id, request : AdvanceAdventure):
    adventure = get_adventure(adventure_id)
    # print(adventure.id)
    if not adventure:
        logger.warning("Adventure was not found when choice was sent")
        raise AdventureNotFound()
    
    if not adventure.is_starting_scene():
        async def event_generator():
            try:
                generator = await adventure.advance_scene(request.choice)
                async for word in generator:
                    yield word        
                logger.info("/choice adventure route completed")
            except Exception as e:
                logger.error(f"streaming failed: {e}")
             
        return StreamingResponse(event_generator(), media_type="text/plain")
    

        