CREATE_ADVENTURES_TABLE = '''
CREATE TABLE IF NOT EXISTS adventures (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    current_story_text TEXT,
    current_story_options TEXT,
    current_scene_number INTEGER,
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

CREATE_ADVENTURES_HISTORY_INDEX = '''
CREATE INDEX IF NOT EXISTS idx_adventure_history_adventure_id
ON adventures_history(adventure_id)
'''

INSERT_ADVENTURE = '''
INSERT INTO adventures(
id, name, current_story_text, current_story_options, current_scene_number, last_chosen_option
)
VALUES(?,?,?,?,?,?)
'''


INSERT_ADVENTURE_HISTORY = '''
INSERT INTO adventures_history(
adventure_id, scene_text, scene_number, chosen_choice
)
VALUES(?,?,?,?) 
'''

GET_ADVENTURE_BY_ID = '''
SELECT * FROM adventures WHERE id = ?
'''

