from pydantic import BaseModel, Field
from typing import Dict, List

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



class AdventuresIdListResponse(BaseModel):
    adventures_ids: List[str] = Field(alias="adventuresIds")

    model_config = {
        "populate_by_name" : True
    }