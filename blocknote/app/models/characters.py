from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from datetime import datetime
from ..database import Base


# Modelos Pydantic para la API

class Character(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    player_id: int
    campaign_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

class CharacterCreate(BaseModel):
    name: str
    description: Optional[str] = None
    player_id: int
    campaign_id: int

class CharacterUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    player_id: Optional[int] = None
    campaign_id: Optional[int] = None

class CharacterDelete(BaseModel):
    id: int