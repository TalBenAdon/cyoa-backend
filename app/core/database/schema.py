from app.core.database.connection import get_connection
from app.core.database.queries import (
    CREATE_ADVENTURES_HISTORY_TABLE,
    CREATE_ADVENTURES_TABLE,
    CREATE_ADVENTURE_HISTORY_INDEX
)

def init_db():
    with get_connection() as conn:
        
   
        cursor = conn.cursor()
        
        cursor.execute(CREATE_ADVENTURES_TABLE)
        cursor.execute(CREATE_ADVENTURES_HISTORY_TABLE)
        cursor.execute(CREATE_ADVENTURE_HISTORY_INDEX)
        
