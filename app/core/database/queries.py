CREATE_ADVENTURES_TABLE = '''
CREATE TABLE IF NOT EXISTS adventures (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    current_story_text TEXT,
    current_story_options TEXT,
    current_story_scene INTEGER,
    last_chosen_option TEXT
)
'''

CREATE_ADVENTURES_HISTORY_TABLE = '''
CREATE TABLE IF NOT EXISTS adventures_history(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    adventure_id TEXT NOT NULL,
    scene_text TEXT NOT NULL,
    scene_number INTEGER,
    chosen_choise TEXT,
    timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (adventure_id) REFERENCES adventures(id)
)
'''

CREATE_ADVENTURE_HISTORY_INDEX = '''
CREATE INDEX IF NOT EXISTS idx_adventure_history_adventure_id
ON adventure_history(adventure_id)
'''

