import requests
import json
from app.core.config import OPENROUTER_KEY
from app.core.logger import get_logger

logger = get_logger(__name__)

def chat_with_ai(prompt: str):

    logger.info("chat with ai initialized")
    
  
    url="http://openrouter.ai/api/v1/chat/completions"
    
    headers={
            "Authorization": f"Bearer {OPENROUTER_KEY}",
            "Content-Type": "application/json",
    },

    payload = {
        "model": "qwen/qwen3-30b-a3b:free",
        "messages":[
                {
                    "role":"user",
                    "content": f"{prompt}"
                }
            ],
    }


    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        return response.json()
    
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error: {e} - Response: {response.text}")

    except requests.exceptions.RequestException as e:
        logger.error(f"Reqeust failed: {e}")

    except KeyError:
        logger.error(f"Unexpected response format: {response.text}")
    
    except Exception as e:
        logger.exception(f"Unexpected error: {e}")