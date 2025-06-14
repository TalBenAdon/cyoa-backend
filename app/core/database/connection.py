import sqlite3
from pathlib import Path
from contextlib import contextmanager

DB_PATH = Path(__file__).resolve().parent.parent.parent / "cyoadb.sqlite"

def get_connection():
    return sqlite3.connect(DB_PATH)


@contextmanager
def db_cursor():
    with get_connection() as conn:
        cursor = conn.cursor()
        try:
            yield cursor
            conn.commit()
        except Exception:
            conn.rollback()
            raise

        