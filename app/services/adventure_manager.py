import json
import sqlite3
from typing import Dict, List
from app.services.adventure_snapshot import AdventureSnapshot
from app.services.adventure import Adventure
from app.core.clients import openrouter_client
from app.core.logger import get_logger
from app.models.adventure import AdventureIdName
from app.core.database.db_helpers import (insert_adventure,
                                          get_adventure_by_id,
                                          get_adventure_history_by_id)

logger = get_logger(__name__)


# temporary adventures data list
adventures : Dict[str, Adventure] = {}

def create_adventure(type: str = "fantasy") -> Adventure:
    adventure = Adventure(openrouter_client, type)
    
    # insert_adventure(adventure)
    
    print("f from create_adventure: {adventure}")
    return adventure








def get_adventures() -> List[AdventureIdName]:
    return [ AdventureIdName(adventure_id = key, adventure_name= value.name) for key, value in adventures.items() ]
    






def get_adventure_with_history(adventure_id : str) -> AdventureSnapshot | None:
    adventure_row = get_adventure_by_id(adventure_id)
    if not adventure_row:
        raise
    
    adventure_history_rows = get_adventure_history_by_id(adventure_id)
    
    adventure_snapshot = AdventureSnapshot(
        adventure_id = adventure_row["id"],
        type = adventure_row["type"],
        scene_number = adventure_row["current_scene_number"],
        history = adventure_history_rows
    )
    
    return adventure_snapshot
    
 
    
    