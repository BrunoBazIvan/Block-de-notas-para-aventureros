from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# Modelos Pydantic para la API

class Weapon(BaseModel):
    id: int # Unique identifier of the weapon
    name: str # Name of the weapon
    category: str # Category of the weapon (e.g., "Simple Melee", "Martial Ranged")
    subtype: Optional[str] = None # Subtype of the weapon (e.g., "Sword", "Bow")
    cost_gp: Optional[str] = None # Cost in gold pieces
    size: Optional[str] = None # Size category of the weapon
    proficiency: Optional[str] = None # Required proficiency
    base_damage: Optional[str] = None # Base damage dice (e.g., "1d8")
    damage_type_id: Optional[int] = None # ID of the damage type
    range_normal: Optional[int] = None # Normal range in feet
    properties: Optional[str] = None # Weapon properties as string
    special: Optional[str] = None # Special weapon properties description
    rarity: Optional[str] = None # Rarity of the weapon
    source_id: Optional[int] = None # ID of the source book
    tags: Optional[str] = None # Tags associated with the weapon
    created_at: datetime # Creation date and time
    updated_at: Optional[datetime] = None # Date and time of the last update

class WeaponCreate(BaseModel):
    name: str # Name of the weapon
    category: str # Category of the weapon
    subtype: Optional[str] = None # Subtype of the weapon
    cost_gp: Optional[str] = None # Cost in gold pieces
    size: Optional[str] = None # Size category of the weapon
    proficiency: Optional[str] = None # Required proficiency
    base_damage: Optional[str] = None # Base damage dice
    damage_type_id: Optional[int] = None # ID of the damage type
    damage_versatile: Optional[str] = None # Versatile damage dice
    range_normal: Optional[int] = None # Normal range in feet
    properties: Optional[str] = None # Weapon properties as string
    special: Optional[str] = None # Special weapon properties description
    rarity: Optional[str] = None # Rarity of the weapon
    source_id: Optional[int] = None # ID of the source book
    tags: Optional[str] = None # Tags associated with the weapon
    min_strength: Optional[int] = None # Minimum strength requirement

class WeaponUpdate(BaseModel):
    name: Optional[str] = None # Updated name of the weapon
    category: Optional[str] = None # Updated category of the weapon
    subtype: Optional[str] = None # Updated subtype of the weapon
    cost_gp: Optional[str] = None # Updated cost in gold pieces
    size: Optional[str] = None # Updated size category
    proficiency: Optional[str] = None # Updated required proficiency
    base_damage: Optional[str] = None # Updated base damage dice
    damage_type_id: Optional[int] = None # Updated damage type ID
    damage_versatile: Optional[str] = None # Updated versatile damage dice
    range_normal: Optional[int] = None # Updated normal range
    properties: Optional[str] = None # Updated weapon properties
    special: Optional[str] = None # Updated special properties description
    rarity: Optional[str] = None # Updated rarity of the weapon
    source_id: Optional[int] = None # Updated source book ID
    tags: Optional[str] = None # Updated tags
    min_strength: Optional[int] = None # Updated minimum strength requirement

class WeaponDelete(BaseModel):
    id: int # Unique identifier of the weapon to be deleted