import json
from queries import INSERT_ADVENTURE
from connection import get_connection
from app.services.adventure import Adventure

def insert_adventure(adventure: Adventure):
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
    