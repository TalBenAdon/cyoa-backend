from fastapi import FastAPI
from app.core.logger import get_logger
from app.api import api_router
logger = get_logger(__name__)

app = FastAPI()

app.include_router(api_router)

@app.get("/")
async def root():
    logger.info("main root accessed")
    return {"message": "MCP root"}