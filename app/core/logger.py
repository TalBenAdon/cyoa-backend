import logging
from app.core.config import LOG_LEVEL, ENV
from colorlog import ColoredFormatter

def get_logger(name: str) -> logging.Logger:

    logger = logging.getLogger(name)
    if not logger.handlers:
        console_handler = logging.StreamHandler()

        if ENV == "development":
            
            formatter = ColoredFormatter(
                "%(asctime)s [%(log_color)s%(levelname)s%(reset)s] %(message)s",
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
               "%(asctime)s [%(levelname)s] %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S", 
            )

        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        logger.setLevel(LOG_LEVEL)
    
    return logger
