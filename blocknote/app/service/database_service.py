from sqlalchemy.orm import Session
from ..database import SessionLocal, engine
from ..models.note import NoteDB, Note, NoteCreate, NoteUpdate
from typing import List, Optional
from datetime import datetime

class NoteService:

    @staticmethod
    def get_db():
        """ Crear una session de base de datos """
        db = SessionLocal()
        try:
            return db
        finally:
            pass

    @staticmethod
    def get_all_notes() -> List[Note]:
        """ Obtener todas las notas """
        db = SessionLocal()
        try: 
            #Consultar todas las notas desde la base de datos 
            db_notes = db.query(NoteDB).all()
            # Convertir los objetos de SQLAlchemy a Pydantic
            notes = []
            for db_note in db_notes:
                note = Note(
                    id=db_note.id,
                    title=db_note.title,
                    content=db_note.content,
                    created_at=db_note.created_at,
                    updated_at=db_note.updated_at
                )
                notes.append(note)

            return notes
        finally:
            db.close()

    @staticmethod
    def get_note_by_id(note_id: int) -> Optional[Note]:
        """ Obtener una nota por su ID """
        db = SessionLocal()
        try:
            # Buscar la nota en la base de datos mediante su id
            db_note = db.query(NoteDB).filter(NoteDB.id == note_id).first()

            if db_note is None:
                return None
            
            # Convertir el objeto de SQLAlchemy a Pydantic
            note = Note(
                id=db_note.id,
                title=db_note.title,
                content=db_note.content,
                created_at=db_note.created_at,
                updated_at=db_note.updated_at
            )
            return note
        finally:
            db.close()
    
    @staticmethod
    def create_note(note_data: NoteCreate) -> Note:
        """ Crear una nueva nota """
        db = SessionLocal()
        try:
            # Crear un objeto de base de datos
            db_note = NoteDB(
                title=note_data.title,
                content=note_data.content,
                created_at=datetime.now(),
            )
            db.add(db_note)
            db.commit()
            db.refresh(db_note)  # Obtener el ID generado

            # Convertir el objeto de SQLAlchemy a Pydantic para retornarlo
            return Note(
                id=db_note.id,
                title=db_note.title,
                content=db_note.content,
                created_at=db_note.created_at,
                updated_at=db_note.updated_at
            )
            
        finally:
            db.close()

    @staticmethod
    def update_note(note_id: int, note_update: NoteUpdate) -> Optional[Note]:
        """ Actualizar una nota existente """
        db = SessionLocal()
        try:
            # Buscar la nota en la base de datos mediante su id
            db_note = db.query(NoteDB).filter(NoteDB.id == note_id).first()

            if db_note is None:
                return None
            
            # Actualizar los campos si se proporcionan
            if note_update.title is not None:
                db_note.title = note_update.title
            if note_update.content is not None:
                db_note.content = note_update.content
            
            # Actualizar el timestamp
            db_note.updated_at = datetime.now()

            # Guardar los cambios en la base de datos
            db.commit()
            db.refresh(db_note)

            # Convertir el objeto de SQLAlchemy a Pydantic para retornarlo
            return Note(
                id=db_note.id,
                title=db_note.title,
                content=db_note.content,
                created_at=db_note.created_at,
                updated_at=db_note.updated_at
            )
        finally:
            db.close()

    @staticmethod
    def delete_note(note_id: int) -> bool:
        """ Eliminar una nota por su ID """
        db = SessionLocal()
        try:
            # Buscar la nota en la base de datos mediante su id
            db_note = db.query(NoteDB).filter(NoteDB.id == note_id).first()

            if db_note is None:
                return False
        
            # Eliminar la nota
            db.delete(db_note)
            db.commit()
            
            return True
        finally:
            db.close()
