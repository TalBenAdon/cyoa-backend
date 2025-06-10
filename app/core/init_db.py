from app.core.database import get_connection


def init_db():
    conn = get_connection()
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
            scene_number INTEGER,
            choices TEXT,
            chosen_choice TEXT,
            timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (adventure_id) REFERENCES adventures(id)
        )
        '''
    )
    