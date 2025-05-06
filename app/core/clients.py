from app.services.adventure import Adventure
from app.services.openrouter_client import OpenRouterClient

openrouter_client = OpenRouterClient()
adventure_client = Adventure(openrouter_client) 