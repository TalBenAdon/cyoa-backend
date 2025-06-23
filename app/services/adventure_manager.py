import json
import sqlite3
from typing import Dict, List
from app.services.adventure_snapshot import AdventureSnapshot
from app.services.adventure import Adventure
from app.core.clients import openrouter_client
from app.core.logger import get_logger
from app.models.adventure import AdventureIdName
from app.core.database.db_helpers import (
                                          get_adventure_by_id,
                                          get_adventure_history_by_id,
                                          return_formatted_history,
                                          get_adventures_names_id_from_db,)


logger = get_logger(__name__)



def create_adventure(type: str = "fantasy") -> Adventure:
    adventure = Adventure(openrouter_client, type)
    
    print(f"from create_adventure: {adventure}")
    return adventure






def get_adventures() -> List[AdventureIdName]:
    adventures = get_adventures_names_id_from_db()
    print(adventures)
    return [AdventureIdName(adventure_id=adventure["id"], adventure_name=adventure["name"]) for adventure in adventures]
   




def get_adventure_with_history_snapshot(adventure_id : str) -> AdventureSnapshot | None:
    adventure_row = get_adventure_by_id(adventure_id)
    if not adventure_row:
        raise
    
    adventure_history_rows = get_adventure_history_by_id(adventure_id)
    formatted_history = return_formatted_history(adventure_history_rows)
    
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

    data = {
        "id": adventure_id,
        "name": adventure_row["name"],
        "type": adventure_row["type"],
        "current_scene_number":adventure_row["current_scene_number"],
        "current_story_text": current_scene_history["scene_text"],
        "last_chosen_option": current_scene_history["chosen_option"],
        "current_story_options": current_scene_history["options"],
        "history": adventure_history_rows
    }

    adventure = Adventure.from_db(openrouter_client,data) 
   
    return adventure


