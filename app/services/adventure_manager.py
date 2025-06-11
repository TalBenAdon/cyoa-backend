import json
from typing import Dict, List
from app.services.adventure import Adventure
from app.core.clients import openrouter_client
from app.core.logger import get_logger
from app.core.database import get_connection
from app.models.adventure import AdventureIdName

logger = get_logger(__name__)


# temporary adventures data list
adventures : Dict[str, Adventure] = {}

def create_adventure(type: str = "fantasy") -> Adventure:
    adventure = Adventure(openrouter_client, type)

    with get_connection() as conn: 
        cursor = conn.cursor()
        cursor.execute(
            '''
            INSERT INTO adventures (
                id, name, current_story_text, current_story_options, current_story_scene, last_chosen_option
                )
                VALUES (?, ?, ?, ?, ?, ?)
            ''',
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