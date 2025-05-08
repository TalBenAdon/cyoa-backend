from pydantic import BaseModel

class StartAdventure(BaseModel):
    type: str | None
    
class AdvanceAdventure(BaseModel):
    choice: str
    adventure_id: str