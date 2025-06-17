import json
from app.core.database.queries import (INSERT_ADVENTURE,
                                       INSERT_ADVENTURE_HISTORY,
                                       GET_ALL_ADVENTURES,
                                       GET_ADVENTURE_BY_ID,
                                       GET_ADVENTURE_HISTORY)
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
                    adventure.type,
                    adventure.current_scene_number
                )
            )
    except Exception as e:
        logger.error(f"Error inserting adventure to database: {e}")


def insert_adventure_history(adventure_id: str, adventure_history: dict):
    try:
        with db_cursor() as cursor:
            cursor.execute(
                INSERT_ADVENTURE_HISTORY,
                (
                    adventure_id,
                    adventure_history["text"],
                    json.dumps(adventure_history["options"]),
                    adventure_history["scene_number"],
                 )
            )
    except Exception as e:
        logger.error(f"Error inserting adventure history to database: {e}")


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


def return_formatted_history(history_array_rows):
    formatted_history = []
    for row in history_array_rows:
        try:
            formatted_history.append({
                "scene_text": row["scene_text"],
                "options": json.loads(row["options"]),
                "scene_number": row["scene_number"]
            })
        except (KeyError, json.JSONDecodeError) as e:
            logger.error(f"Error formatting history entries: {e}")
    return formatted_history

        
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
        with db_cursor() as cursor:
            cursor.execute(
                GET_ADVENTURE_HISTORY,
                (adventure_id,)
            )
            rows = cursor.fetchall()
            return[dict(row) for row in rows]
        
    except Exception as e:
         logger.error(f"Error fetching adventure's from database: {e}")
         