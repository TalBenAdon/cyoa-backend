import requests
import json
from app.core.config import OPENROUTER_KEY, OPENROUTER_URL
from app.core.logger import get_logger

logger = get_logger(__name__)


model = "qwen/qwen3-30b-a3b:free"

class OpenRouterClient:

    def __init__(self, api_key: str = OPENROUTER_KEY):
        self.api_key = api_key
        self.url = OPENROUTER_URL
    
        self.headers = {
            "Authorization":f"Bearer {OPENROUTER_KEY}",
             "Content-Type": "application/json"
        }

    def chat(self, prompt : str) -> str | None :
        logger.info("chat with ai initialized")

        payload = {
        "model": model, #currently hard coding free model for testing
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
    
        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP error: {e} - Response: {response.text}")

        except requests.exceptions.RequestException as e:
            logger.error(f"Reqeust failed: {e}")

        except KeyError:
            logger.error(f"Unexpected response format: {response.text}")
    
        except Exception as e:
            logger.exception(f"Unexpected error: {e}")
        

    