from pydantic import BaseModel, Field
from typing import List

class StartAdventure(BaseModel):
    type: str | None



class AdvanceAdventure(BaseModel):
    choice: str


 


class HistoryEntry(BaseModel):
    text: str
    options:List[str]
    scene:int

class AdventureInfoResponse(BaseModel):
    id: str
    type: str
    scene_number: int = Field(alias="sceneNumber")
    history: List[HistoryEntry]

    model_config = {
        "populate_by_name" : True
    }



class AdventureIdName(BaseModel):
    adventure_id: str = Field(alias="adventureId")
    adventure_name:str = Field(alias="adventureName")
    model_config = {
        "populate_by_name" : True
    }
    
class AdventuresIdListResponse(BaseModel):
    adventures: List[AdventureIdName]
