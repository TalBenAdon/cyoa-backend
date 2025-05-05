import httpx
from typing import AsyncGenerator
import json
from app.exceptions import OpenRouterAPIException, InvalidAIResponse, BaseAppException
from app.core.config import OPENROUTER_KEY, OPENROUTER_URL
from app.core.logger import get_logger

logger = get_logger(__name__)


model = "qwen/qwen3-30b-a3b:free" #currently hard coding free model for testing
# model = "deepseek/deepseek-chat-v3-0324:free" #currently hard coding free model for testing

class OpenRouterClient:

    def __init__(self, api_key: str = OPENROUTER_KEY):
        self.api_key = api_key
        self.url = OPENROUTER_URL

        self.headers = {
            "Authorization":f"Bearer {OPENROUTER_KEY}",
             "Content-Type": "application/json"
        }

    async def chat_with_ai(self, system_message : str,user_message : str) -> AsyncGenerator[str , None] : 
        logger.info("chat with ai initialized")

        payload = {
        "model": model, 
        "stream": True,
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
            async with httpx.AsyncClient(timeout=None) as client:
                async with client.stream("POST",self.url, headers=self.headers, json=(payload)) as response:
                # response = await client.post(self.url, headers=self.headers, json=(payload))
                    async for line in response.aiter_lines():
                        print(line)
                        if line.startswith("data: "):
                            raw = line.removeprefix("data: ").strip()
                            if raw == "[DONE]":
                                break
                            try:
                                chunk = json.loads(raw)
                                delta = chunk["choices"][0]["delta"]
                                if "content" in delta:
                                    yield delta["content"]
                            except(KeyError, json.JSONDecodeError) as e:
                                logger.warning(f"Stream chunk error: {e} - Raw {raw}")
            

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
        

    