import json
import sqlite3
from typing import Dict, List
from app.services.adventure import Adventure
from app.core.clients import openrouter_client
from app.core.logger import get_logger
from app.core.database.connection import get_connection
from app.models.adventure import AdventureIdName
from app.core.database.db_helpers import insert_adventure
from app.core.database.queries import (
    INSERT_ADVENTURE,
    GET_ADVENTURE_BY_ID
)
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
    with get_connection() as conn:
        try:
            print(f"my id: {adventure_id}")
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(
            GET_ADVENTURE_BY_ID,
            (adventure_id,)
            )
            row = cursor.fetchone()
            row = dict(row)
            print(f" the row is there: {row}")
            # print(dict(row))
            return dict(row) if row else None
        
        except Exception as e:
            logger.error(f"failed fetching requested adventure {e}")
            return None