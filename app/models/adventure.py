from pydantic import BaseModel

class StartAdventure(BaseModel):
    type: str | None