import os
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
ENV = os.getenv("ENV", "development")
LOG_DIR = os.getenv("LOG_DIR", "logs")