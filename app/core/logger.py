import logging
from app.core.config import LOG_LEVEL

def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        logging.basicConfig(
            level=LOG_LEVEL,
            format="%(asctime)s [%(levelname)s] %(message)s",
        )
    return logger