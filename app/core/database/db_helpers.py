import json
from app.core.database.queries import (INSERT_ADVENTURE, GET_ALL_ADVENTURES, GET_ADVENTURE_BY_ID)
from app.core.database.connection import db_cursor
from app.services.adventure import Adventure
from app.core.logger import get_logger

logger = get_logger(__name__)


def insert_adventure(adventure: Adventure):
    try:
        with db_cursor() as cursor:
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

    except Exception as e:
        logger.error(f"Error inserting adventure to database: {e}")

        
def get_adventures_from_db():
    try:
        with db_cursor() as cursor:
           cursor.execute(
               GET_ALL_ADVENTURES
           )
           rows = cursor.fetchall()
           return [dict(row) for row in rows]
            
    except Exception as e:
        logger.error(f"Error fetching adventures from database: {e}")
        
        
def get_adventure_by_id(adventure_id :str):
    try:
        with db_cursor() as cursor:
            cursor.execute(
                GET_ADVENTURE_BY_ID,
                (adventure_id,)
            )
            row = cursor.fetchone()
        return dict(row)
    
    except Exception as e:
         logger.error(f"Error fetching adventure from database: {e}")
         
         
def get_adventure_history_by_id(adventure_id: str):
    try:
        
    except Exception as e:
         logger.error(f"Error fetching adventure's from database: {e}")
         