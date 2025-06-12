import json
from typing import Dict, List
from app.services.adventure import Adventure
from app.core.clients import openrouter_client
from app.core.logger import get_logger
from app.core.database.connection import get_connection
from app.models.adventure import AdventureIdName
from app.core.database.queries import (
    INSERT_ADVENTURE
)
logger = get_logger(__name__)


# temporary adventures data list
adventures : Dict[str, Adventure] = {}

def create_adventure(type: str = "fantasy") -> Adventure:
    adventure = Adventure(openrouter_client, type)

    with get_connection() as conn: 
        cursor = conn.cursor()
        cursor.execute(
        INSERT_ADVENTURE,
            (
            adventure.id,
            adventure.name,
            adventure.current_story_text,
           json.dumps(adventure.current_story_options or {}),
            adventure.scene_num,
            adventure.last_chosen_option
            )
        )
    
    return 




def get_adventures() -> List[AdventureIdName]:
    return [ AdventureIdName(adventure_id = key, adventure_name= value.name) for key, value in adventures.items() ]
    






def get_adventure(adventure_id : str) -> Adventure | None:
    return adventures.get(adventure_id)