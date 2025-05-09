from pydantic import BaseModel
from typing import Dict, List

class StartAdventure(BaseModel):
    type: str | None
    
class AdvanceAdventure(BaseModel):
    choice: str
    adventure_id: str

class AdventureInfo(BaseModel):
    id: str
    type: str
    scene_number: int
    history: List[Dict]

class AdventuresIdList(BaseModel):
    adventures_ids: List[str]