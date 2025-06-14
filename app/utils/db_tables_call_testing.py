from app.core.database.connection import get_connection
from app.core.logger import get_logger

logger = get_logger(__name__)

def log_all_table_names():
    with get_connection() as conn:
        cursor = conn.cursor()

      
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        for (table_name,) in tables:
            logger.info(f"--- Contents of '{table_name}' ---")
            try:
                cursor.execute(f"SELECT * FROM {table_name}")
                rows = cursor.fetchall()
                if not rows:
                    logger.info(" (empty)")
                else:
                    for row in rows:
                        logger.info(row)
            except Exception as e:
                logger.error(f"Failed to read from {table_name}: {e}")