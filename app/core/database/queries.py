CREATE_ADVENTURES_TABLE = '''
CREATE TABLE IF NOT EXISTS adventures (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    current_scene_number INTEGER NOT NULL
)
'''

CREATE_ADVENTURES_HISTORY_TABLE = '''
CREATE TABLE IF NOT EXISTS adventures_history(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    adventure_id TEXT NOT NULL,
    scene_text TEXT NOT NULL,
    options TEXT NOT NULL,
    chosen_option TEXT,
    scene_number INTEGER NOT NULL,
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
id, name, type, current_scene_number
)
VALUES(?,?,?,?)
'''


INSERT_ADVENTURE_HISTORY = '''
INSERT INTO adventures_history(
adventure_id, scene_text, options, scene_number
)
VALUES(?,?,?,?) 
'''

UPDATE_HISTORY_CHOSEN_OPTION = '''
UPDATE adventures_history
SET chosen_option = ?
WHERE adventure_id = ? AND scene_number = ?
'''


UPDATE_ADVENTURE_SCENE_NUMBER = '''
UPDATE adventures
SET current_scene_number = ?
WHERE id = ?
'''


GET_ADVENTURE_BY_ID = '''
SELECT * FROM adventures WHERE id = ?
'''


GET_ALL_ADVENTURES = '''
SELECT id, name FROM adventures
'''

GET_ADVENTURE_HISTORY = '''
SELECT * FROM adventures_history WHERE adventure_id = ?
'''