import logging
import logging.handlers
from app.core.config import LOG_LEVEL, ENV, LOG_DIR
from colorlog import ColoredFormatter
import os

os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE=os.path.join(LOG_DIR, "app.log")

colored_format = "%(asctime)s [%(log_color)s%(levelname)s%(reset)s] %(name)s - %(message)s"
normal_format =  "%(asctime)s [%(levelname)s] %(name)s - %(message)s"

def get_logger(name: str) -> logging.Logger:

    logger = logging.getLogger(name)
    if not logger.handlers:
        console_handler = logging.StreamHandler()

        if ENV == "development":
            
            formatter = ColoredFormatter(
                colored_format,
                datefmt="%Y-%m-%d %H:%M:%S",
                log_colors={
                    'DEBUG': 'cyan',
                    'INFO' : 'green',
                    'WARNING': 'yellow',
                    'ERROR': 'red',
                    'CRITICAL': 'bold_red',
                }
            )

        else:
            formatter = logging.Formatter(
               normal_format,
                datefmt="%Y-%m-%d %H:%M:%S", 
            )

        file_handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=5*1024*1024, backupCount=3, encoding="utf-8")
        
        file_formatter = logging.Formatter(
            normal_format
        )

        console_handler.setFormatter(formatter)
        file_handler.setFormatter(file_formatter)
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
        logger.setLevel(LOG_LEVEL)
    
    return logger
