from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from datetime import datetime
from ..database import Base


# Modelos Pydantic para la API

class Campaign(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    master_id: int
    is_active: bool = True
    created_at: datetime
    updated_at: Optional[datetime] = None

class CampaignCreate(BaseModel):
    name: str
    description: Optional[str] = None
    master_id: int

class CampaignUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None

class CampaignDelete(BaseModel):
    id: int