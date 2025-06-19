import json
import sqlite3
from typing import Dict, List
from app.services.adventure_snapshot import AdventureSnapshot
from app.utils.create_ai_context_from_db import create_ai_context_from_db
from app.services.adventure import Adventure
from app.core.clients import openrouter_client
from app.core.logger import get_logger
from app.models.adventure import AdventureIdName
from app.core.database.db_helpers import (
                                          get_adventure_by_id,
                                          get_adventure_history_by_id,
                                          return_formatted_history)

logger = get_logger(__name__)



def create_adventure(type: str = "fantasy") -> Adventure:
    adventure = Adventure(openrouter_client, type)
    
    print(f"from create_adventure: {adventure}")
    return adventure






def get_adventures() -> List[AdventureIdName]:
    return [ AdventureIdName(adventure_id = key, adventure_name= value.name) for key, value in adventures.items() ] #TODO update to gather from db
    




def get_adventure_with_history_snapshot(adventure_id : str) -> AdventureSnapshot | None:
    adventure_row = get_adventure_by_id(adventure_id)
    if not adventure_row:
        raise
    
    adventure_history_rows = get_adventure_history_by_id(adventure_id)
    formatted_history = return_formatted_history(adventure_history_rows)
    
    print(f" my history rows{adventure_history_rows}")
    adventure_snapshot = AdventureSnapshot(
        adventure_id = adventure_row["id"],
        type = adventure_row["type"],
        scene_number = adventure_row["current_scene_number"],
        history = formatted_history
    )
    
    return adventure_snapshot
 
    
def get_adventure(adventure_id : str)-> Adventure:  

    adventure_row = get_adventure_by_id(adventure_id)
    adventure_history_rows = get_adventure_history_by_id(adventure_id)

    current_scene_num = adventure_row["current_scene_number"]

    if current_scene_num != adventure_history_rows[-1]["scene_number"]:
        raise Exception #TODO create an error for when current scene num doesnt match the last history scene
    
    current_scene_history = adventure_history_rows[current_scene_num-1]

    create_ai_context_from_db(adventure_row["type"], adventure_history_rows) #TODO create the context

    data = {
        "id": adventure_id,
        "name": adventure_row["name"],
        "type": adventure_row["type"],
        "current_scene_number":adventure_row["current_scene_number"],
        "current_story_text": current_scene_history["scene_text"],
        "last_chosen_option": current_scene_history["chosen_option"],
        "current_story_options": current_scene_history["options"]
    }

    adventure = Adventure.from_db(openrouter_client,data) #TODO return the adventure and see if its usable for other api calls


