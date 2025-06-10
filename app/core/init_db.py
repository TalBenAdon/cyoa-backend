from app.core.database import get_connection


def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS adventures (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            
        )
        '''
    )
    