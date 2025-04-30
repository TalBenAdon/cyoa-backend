from fastapi import APIRouter, HTTPException
from app.services.openrouter_client import OpenRouterClient
from app.models.ai import PromptRequest
from app.core.logger import get_logger

logger = get_logger(__name__)

router = APIRouter()
client = OpenRouterClient()

@router.post("/chat")
async def chat(request: PromptRequest):
    logger.info("/chat api route accessed")

    try:
        result = client.chat(request.prompt)

        if result is None:
            logger.error("Ai response failed in @post /chat")
            raise HTTPException(status_code=500, detail="AI response failed.")
        
        logger.info("/chat api route completed")
        return {"response": result}

    except Exception as e:
        logger.exception("Unexpected error in /chat endpoint")
        raise HTTPException(status_code=500, detail="AI response failed.")


