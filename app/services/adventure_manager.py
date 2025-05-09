from typing import Dict, List
from app.services.adventure import Adventure
from app.core.clients import openrouter_client

# temporary adventures data list
adventures : Dict[str, Adventure] = {}

def create_adventure(type: str = "fantasy") -> Adventure:
    adventure = Adventure(openrouter_client, type)
    adventures[adventure.id] = adventure
    return adventure




def get_adventures_ids() -> List[str]:
    return list(adventures.keys())






def get_adventure(adventure_id : str) -> Adventure | None:
    return adventures.get(adventure_id)