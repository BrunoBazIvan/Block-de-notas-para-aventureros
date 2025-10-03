from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from ..database import Base

#Models for SQLAlchemy 
class NoteDB(Base):
    __tablename__ = "notes"
    id = Column (Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, nullable=True)
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