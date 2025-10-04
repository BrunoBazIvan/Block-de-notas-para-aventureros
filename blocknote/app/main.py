from fastapi import FastAPI, HTTPException, APIRouter
from fastapi.middleware.cors import CORSMiddleware 
from datetime import datetime 
from .models.note import Note, NoteCreate, NoteUpdate
from .service.database_service import NoteService



app = FastAPI()

# Crear router para las APIs
api_router = APIRouter(prefix="/api")

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las fuentes (en producción, especificar dominios)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@api_router.get("/notes")
def get_notes():
    """ Obtener todas las notas """
    try:
        notes = NoteService.get_all_notes()
        return notes
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@api_router.get("/notes/{note_id}")
def get_note_by_id(note_id: int):
    """ Obtener una Nota por su id"""
    try:
        note = NoteService.get_note_by_id(note_id)
        if note is None:
            raise HTTPException(status_code=404, detail="Note not found")
        return note
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@api_router.post("/notes")
def create_note_endpoint(note: NoteCreate):
    """ Crear una nota nueva """
    try:
        new_note = NoteService.create_note(note)
        return new_note
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@api_router.put("/notes/{note_id}")
def update_note_endpoint(note_id: int, note_update: NoteUpdate):
    """ Actualizar una nota """
    try:
        updated_note = NoteService.update_note(note_id, note_update)
        if updated_note is None:
            raise HTTPException(status_code=404, detail="Note not found")
        return updated_note
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@api_router.delete("/notes/{note_id}")
def delete_note_endpoint(note_id: int):
    """ Borrar una nota """
    try:
        note = NoteService.delete_note(note_id)
        if note is None:
            raise HTTPException(status_code=404, detail="Note not found")
        return {"message": "Note deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Incluir el router en la aplicación
app.include_router(api_router)

# === ENDPOINTS SIN PREFIJO (compatibilidad) ===

@app.get("/notes")
def get_notes_compat():
    """Endpoint de compatibilidad sin prefijo /api"""
    return get_notes()

@app.get("/notes/{note_id}")
def get_note_by_id_compat(note_id: int):
    """Endpoint de compatibilidad sin prefijo /api"""
    return get_note_by_id(note_id)

@app.post("/notes")
def create_note_compat(note: NoteCreate):
    """Endpoint de compatibilidad sin prefijo /api"""
    return create_note_endpoint(note)

@app.put("/notes/{note_id}")
def update_note_compat(note_id: int, note_update: NoteUpdate):
    """Endpoint de compatibilidad sin prefijo /api"""
    return update_note_endpoint(note_id, note_update)

@app.delete("/notes/{note_id}")
def delete_note_compat(note_id: int):
    """Endpoint de compatibilidad sin prefijo /api"""
    return delete_note_endpoint(note_id)

# Endpoint de salud
@app.get("/")
def root():
    return {"message": "Block de Notas Aventurero API funcionando correctamente!"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "database": "connected"}