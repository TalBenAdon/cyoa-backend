import json
from queries import INSERT_ADVENTURE
from connection import get_connection
from app.services.adventure import Adventure
from app.core.logger import get_logger

logger = get_logger(__name__)

def insert_adventure(adventure: Adventure):
    try:
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
    except Exception as e:
        logger.error(f"Error inserting adventure to database{e}")