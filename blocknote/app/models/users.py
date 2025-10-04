from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from datetime import datetime
from ..database import Base

# Main User Model
class User(BaseModel):
    id: int # Unique identifier of the user
    player_id: int # ID of the player associated with the user
    master_id: int # ID of the game master associated with the user
    email: str # Email of the user
    name: str # Name of the user
    created_at: datetime # Creation date and time
    updated_at: Optional[datetime] = None # Date and time of the last update

# Model for creating a new User
class UserCreate(BaseModel):
    email: str # Email of the user
    name: str # Name of the user
    password: str # Password of the user

class UserUpdate(BaseModel):
    email: Optional[str] = None # Updated email of the user
    name: Optional[str] = None # Updated name of the user
    password: Optional[str] = None # Updated password of the user

# Model for deleting a User
class UserDelete(BaseModel):
    id: int # Unique identifier of the user to be deleted