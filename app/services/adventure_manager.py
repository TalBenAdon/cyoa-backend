from typing import Dict
from app.services.adventure import Adventure
from app.core.clients import openrouter_client


adventures : Dict[str, Adventure] = {}

def create_adventure(type: str = "fantasy") -> Adventure:
    adventure = Adventure(openrouter_client, type)
    adventures[adventure.id] = adventure
    return adventure

