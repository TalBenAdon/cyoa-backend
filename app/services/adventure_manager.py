import json
import sqlite3
from typing import Dict, List
from app.services.adventure import Adventure
from app.core.clients import openrouter_client
from app.core.logger import get_logger
from app.models.adventure import AdventureIdName
from app.core.database.db_helpers import insert_adventure, get_adventure_by_id

logger = get_logger(__name__)


# temporary adventures data list
adventures : Dict[str, Adventure] = {}

def create_adventure(type: str = "fantasy") -> Adventure:
    adventure = Adventure(openrouter_client, type)
    
    insert_adventure(adventure)
    
    print("f from create_adventure: {adventure}")
    return adventure








def get_adventures() -> List[AdventureIdName]:
    return [ AdventureIdName(adventure_id = key, adventure_name= value.name) for key, value in adventures.items() ]
    






def get_adventure(adventure_id : str) -> Adventure | None:
    adventure = get_adventure_by_id(adventure_id)
    if adventure:
        return adventure
    raise