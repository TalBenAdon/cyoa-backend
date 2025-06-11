from app.core.database.database import get_connection


def init_db():
    with get_connection() as conn:
        
   
        cursor = conn.cursor()
        
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS adventures (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                current_story_text TEXT,
                current_story_options TEXT,
                current_story_scene INTEGER,
                last_chosen_option TEXT
            )
            '''
        )
        
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS adventures_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                adventure_id TEXT NOT NULL,
                scene_text TEXT NOT NULL,
                scene_number INTEGER,
                choices TEXT NOT NULL,
                chosen_choice TEXT,
                timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (adventure_id) REFERENCES adventures(id)
            )
            '''
        )

        cursor.execute(
            '''
            CREATE INDEX IF NOT EXISTS idx_adventure_history_adventure_id
            ON adventure_history(adventure_id)
            '''
        )
        
