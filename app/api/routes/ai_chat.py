from fastapi import APIRouter
from app.services.openrouter_client import OpenRouterClient
from app.models.ai import PromptRequest
from app.core.logger import get_logger
from app.core.clients import openrouter_client
logger = get_logger(__name__)

router = APIRouter()


@router.post("/chat")
async def chat(request: PromptRequest):
    logger.info("/chat api route accessed")
            
    result = openrouter_client.chat(request.prompt)
            
    logger.info("/chat api route completed")
    return {"response": result}

