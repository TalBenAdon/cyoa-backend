from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.services.openrouter_client import OpenRouterClient
from app.models.ai import PromptRequest
from app.core.logger import get_logger
from app.core.clients import openrouter_client
logger = get_logger(__name__)

router = APIRouter()


@router.post("/chat")
async def chat(request: PromptRequest):
    logger.info("/chat api route accessed")
    async def event_generator():
        async for word in openrouter_client.chat_with_ai("hi", "hi"):
            print(word)
            yield word        
    
            
    logger.info("/chat api route completed")
    return StreamingResponse(event_generator(), media_type="text/plain")

