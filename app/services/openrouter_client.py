import httpx

import json
from app.exceptions import OpenRouterAPIException, InvalidAIResponse, BaseAppException
from app.core.config import OPENROUTER_KEY, OPENROUTER_URL
from app.core.logger import get_logger

logger = get_logger(__name__)


model = "qwen/qwen3-30b-a3b:free" #currently hard coding free model for testing

class OpenRouterClient:

    def __init__(self, api_key: str = OPENROUTER_KEY):
        self.api_key = api_key
        self.url = OPENROUTER_URL

        self.headers = {
            "Authorization":f"Bearer {OPENROUTER_KEY}",
             "Content-Type": "application/json"
        }

    async def chat_with_ai(self, system_message : str,user_message : str) -> str : 
        logger.info("chat with ai initialized")

        payload = {
        "model": model, 
        "messages":[
                {
                "role": "system",
                "content" : system_message
                },
                {
                    "role":"user",
                    "content": user_message
                }
            ],
    }
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(self.url, headers=self.headers, json=(payload))
                response.raise_for_status()
                logger.info(f"AI response: {response.json()}")
                content = response.json()["choices"][0]["message"]["content"]
                parsed_content = json.loads(content) #AI replies with a big string, not actual JSON object
                return parsed_content

        except httpx.TimeoutException:
            logger.warning("Timeout when calling OpenROuter")
            raise OpenRouterAPIException("OpenRouter timeout")
        
        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error from: {OPENROUTER_URL} - Response: {e.response.text}")
            raise OpenRouterAPIException(f"HTTP error: {e.response.status_code}")

        except httpx.RequestError as e:
            logger.error(f"Request failed while calling {OPENROUTER_URL}: {e.response.text}")
            raise OpenRouterAPIException("OpenRouter request failed") from e

        except KeyError:
            logger.error(f"Unexpected response format: {response.text}")
            raise InvalidAIResponse("Invalid AI response format")
    
        except Exception as e:
            logger.exception(f"Unexpected error: {e}")
            raise BaseAppException("AI service failure") from e
        

    