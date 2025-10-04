from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from datetime import datetime
from ..database import Base

# Main Note Model
class Note(BaseModel):
    id: int # Unique identifier of the note
    title: str # Title of the note
    content: str # Content of the note
    created_at: datetime # Creation date and time
    updated_at: Optional[datetime] = None # Date and time of the last update

# Model for creating a new Note
class NoteCreate(BaseModel):
    title: str # Title of the note
    content: str # Content of the note

# Model for updating an existing Note
class NoteUpdate(BaseModel):
    title: Optional[str] = None # Updated title of the note
    content: Optional[str] = None # Updated content of the note

class NoteDelete(BaseModel):
    id: int # Unique identifier of the note to be deleted