from app.core.database.connection import get_connection
from app.core.logger import get_logger

logger = get_logger(__name__)

def log_and_return_all_tables():
    with get_connection() as conn:
        cursor = conn.cursor()

      
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        database_visualization = []
        
        for (table_name,) in tables:
            logger.info(f"--- Contents of '{table_name}' ---")
            try:
                table_entry = {table_name: []}
                database_visualization.append(table_entry)
                cursor.execute(f"SELECT * FROM {table_name}")
                rows = cursor.fetchall()
                if not rows:
                    logger.info(" (empty)")
                else:
                    for row in rows:
                        table_entry[table_name].append(row)
                        logger.info(dict(row))
            
            except Exception as e:
                logger.error(f"Failed to read from {table_name}: {e}")