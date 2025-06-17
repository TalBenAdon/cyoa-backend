from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from app.core.logger import get_logger
from app.api import api_router
from app.core.database.schema import init_db
logger = get_logger(__name__)

init_db()

app = FastAPI()

app.include_router(api_router)

app.add_middleware(
CORSMiddleware,
allow_origins = ["http://localhost:5173"],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
expose_headers=["X-Adventure-ID"]
)


@app.get("/")
async def root():
    logger.info("main root accessed")
    return {"message": "MCP root"}


