from fastapi import FastAPI
from app.core.logger import get_logger

logger = get_logger(__name__)

app = FastAPI()

@app.get("/")
async def root():
    logger.info("main root accessed")
    return {"message": "MCP root"}