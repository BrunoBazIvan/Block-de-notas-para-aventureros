from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from datetime import datetime
from ..database import Base


# Modelos Pydantic para la API

class InventoryItem(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    quantity: int
    price: float
    rarity: Optional[str] = None
    magical: bool = False
    player_id: int
    campaign_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

class InventoryItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    quantity: int
    price: float
    rarity: Optional[str] = None
    magical: bool = False
    player_id: int
    campaign_id: int

class InventoryItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    quantity: Optional[int] = None
    price: Optional[float] = None
    rarity: Optional[str] = None
    magical: Optional[bool] = None
    player_id: Optional[int] = None
    campaign_id: Optional[int] = None
    name: str
    description: Optional[str] = None
    player_id: int
    campaign_id: int

class InventoryItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    quantity: Optional[int] = None
    price: Optional[float] = None
    rarity: Optional[str] = None
    magical: Optional[bool] = None
    player_id: Optional[int] = None
    campaign_id: Optional[int] = None

class InventoryItemDelete(BaseModel):
    id: int