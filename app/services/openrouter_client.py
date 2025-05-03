import requests
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

    def chat(self, prompt : str) -> str :
        logger.info("chat with ai initialized")

        payload = {
        "model": model, 
        "messages":[
                {
                    "role":"user",
                    "content": f"{prompt}"
                }
            ],
    }
        try:
            response = requests.post(self.url, headers=self.headers, data=json.dumps(payload))
            response.raise_for_status()
            logger.info(f"AI response: {response.json()}")
            return response.json()["choices"][0]["message"]["content"]

        except requests.exceptions.Timeout:
            logger.warning("Timeout when calling OpenROuter")
            raise OpenRouterAPIException("OpenRouter timeout")
        
        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP error from: {OPENROUTER_URL} - Response: {e.response.text}")
            raise OpenRouterAPIException(f"HTTP error: {e.response.status_code}")

        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed while calling {OPENROUTER_URL}: {e.response.text}")
            raise OpenRouterAPIException("OpenRouter request failed") from e

        except KeyError:
            logger.error(f"Unexpected response format: {response.text}")
            raise InvalidAIResponse("Invalid AI response format")
    
        except Exception as e:
            logger.exception(f"Unexpected error: {e}")
            raise BaseAppException("AI service failure") from e
        

    