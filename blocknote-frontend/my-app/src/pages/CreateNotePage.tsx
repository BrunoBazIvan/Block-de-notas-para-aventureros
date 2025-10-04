import { ApiService } from "../ApiService";
import { useState, useEffect } from "react";
import type { Note } from '../ApiService';
import './CreateNotePage.css';

const CreateNotePage = () => {
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [previousNote, setPreviousNote] = useState<Note | null>(null);
  const [loadingPreviousNote, setLoadingPreviousNote] = useState(false);
  const [currentNoteIndex, setCurrentNoteIndex] = useState(0);
  const [allNotes, setAllNotes] = useState<Note[]>([]);

  // Cargar todas las notas
  const loadAllNotes = async () => {
    setLoadingPreviousNote(true);
    try {
      const response = await ApiService.getAllNotes();
      const notes = response.data || [];
      if (notes.length > 0) {
        // Ordenar por fecha de creación descendente
        const sortedNotes = notes.sort((a: Note, b: Note) => 
          new Date(b.created_at).getTime() - new Date(a.created_at).getTime()
        );
        setAllNotes(sortedNotes);
        setPreviousNote(sortedNotes[currentNoteIndex]);
      }
    } catch (error) {
      console.error("Error al cargar notas:", error);
    } finally {
      setLoadingPreviousNote(false);
    }
  };

  useEffect(() => {
    loadAllNotes();
  }, []); // eslint-disable-line react-hooks/exhaustive-deps

  useEffect(() => {
    if (allNotes.length > 0) {
      setPreviousNote(allNotes[currentNoteIndex] || null);
    }
  }, [currentNoteIndex, allNotes]);

  // Navegación entre notas
  const goToPreviousNote = () => {
    if (currentNoteIndex < allNotes.length - 1) {
      setCurrentNoteIndex(currentNoteIndex + 1);
    }
  };

  const goToNextNote = () => {
    if (currentNoteIndex > 0) {
      setCurrentNoteIndex(currentNoteIndex - 1);
    }
  };

  const handleCreateNote = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!title.trim() || !content.trim()) {
      alert("Por favor, completa todos los campos del pergamino");
      return;
    }

    setIsLoading(true);
    
    try {
      const noteData = {
        title: title.trim(),
        content: content.trim(),
      };
      
      const response = await ApiService.createNote(noteData);
      console.log("Nota creada:", response.data);
      
      // Limpiar el formulario después de crear la nota
      setTitle("");
      setContent("");
      
      alert("¡Tu aventura ha sido registrada en el libro de crónicas!");
      
      // Recargar las notas para mostrar la nueva
      await loadAllNotes();
      setCurrentNoteIndex(0); // Mostrar la nota más reciente
    } catch (error) {
      console.error("Error al crear la nota:", error);
      alert("Los antiguos hechizos fallan... Inténtalo de nuevo.");
    } finally {
      setIsLoading(false);
    }
  };

  const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleDateString('es-ES', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  const truncateContent = (content: string, maxLength: number = 400) => {
    if (content.length <= maxLength) return content;
    return content.substring(0, maxLength) + '...';
  };
  
  return (
    <div className="medieval-workshop">
      <div className="workshop-atmosphere">
        <div className="candle-light"></div>
        <div className="dust-particles"></div>
        <div className="floating-embers"></div>
      </div>
      
      {/* Botón de navegación izquierdo */}
      <button 
        className={`nav-arrow nav-left ${currentNoteIndex >= allNotes.length - 1 ? 'disabled' : ''}`}
        onClick={goToPreviousNote}
        disabled={currentNoteIndex >= allNotes.length - 1 || isLoading}
        title="Nota anterior"
      >
        <span className="arrow-icon">◀</span>
      </button>
      
      <div className="ancient-tome">
        <div className="tome-cover">
          <div className="cover-ornament">⚜</div>
          <h1 className="tome-title">Crónicas de Aventureros</h1>
          <div className="cover-subtitle">Libro de Memorias Épicas</div>
          <div className="leather-texture"></div>
          <div className="metal-corner top-left"></div>
          <div className="metal-corner top-right"></div>
          <div className="metal-corner bottom-left"></div>
          <div className="metal-corner bottom-right"></div>
        </div>
        
        <div className="double-page-spread">
          {/* Página Izquierda - Nota Anterior */}
          <div className="left-page">
            <div className="page-binding left-binding"></div>
            <div className="previous-note-container">
              {loadingPreviousNote ? (
                <div className="loading-previous">
                  <div className="ancient-scroll">📜</div>
                  <p>Buscando en los archivos antiguos...</p>
                </div>
              ) : previousNote ? (
                <div className="previous-note">
                  <div className="note-header">
                    <div className="note-ornament">🏰</div>
                    <h3 className="previous-title">{previousNote.title}</h3>
                    <div className="note-date">
                      {formatDate(previousNote.created_at)}
                    </div>
                  </div>
                  <div className="note-content-display">
                    <div className="content-scroll">
                      {truncateContent(previousNote.content).split('\n').map((paragraph, index) => (
                        <p key={index} className="content-paragraph">
                          {paragraph}
                        </p>
                      ))}
                    </div>
                  </div>
                  <div className="note-footer">
                    <div className="previous-note-label">~ Aventura Registrada ~</div>
                    <div className="note-counter">
                      {allNotes.length > 0 ? `${currentNoteIndex + 1} de ${allNotes.length}` : ''}
                    </div>
                  </div>
                </div>
              ) : (
                <div className="empty-previous">
                  <div className="empty-scroll">📜</div>
                  <h3>Libro Nuevo</h3>
                  <p>Aún no hay aventuras previas registradas en este tomo épico.</p>
                  <p>Comenzarás tu primera crónica legendaria en la página derecha.</p>
                </div>
              )}
            </div>
          </div>
          
          {/* Página Derecha - Nueva Nota */}
          <div className="right-page">
            <div className="page-binding right-binding"></div>
            <div className="ink-stains"></div>
            
            <form onSubmit={handleCreateNote} className="adventure-form">
              <div className="form-header">
                <div className="quill-ornament">🖋️</div>
                <h2 className="form-title">Nueva Aventura</h2>
              </div>
              
              <div className="title-section">
                <label className="medieval-label">
                  <span className="label-ornament">✦</span>
                  Título de la Aventura
                  <span className="label-ornament">✦</span>
                </label>
                <input 
                  type="text" 
                  className="medieval-title-input"
                  placeholder="Escribe el nombre de tu aventura..."
                  value={title}
                  onChange={(e) => setTitle(e.target.value)}
                  disabled={isLoading}
                  required
                />
                <div className="title-underline"></div>
              </div>
              
              <div className="content-section">
                <label className="medieval-label">
                  <span className="label-ornament">❦</span>
                  Crónica de la Aventura
                  <span className="label-ornament">❦</span>
                </label>
                <textarea 
                  className="medieval-content-textarea"
                  placeholder="Narra aquí los detalles de tu épica aventura...\n\nCuéntanos sobre los lugares que visitaste, los desafíos que enfrentaste, los tesoros que encontraste y los compañeros que conociste en el camino..."
                  value={content}
                  onChange={(e) => setContent(e.target.value)}
                  disabled={isLoading}
                  required
                  rows={10}
                />
              </div>
              
              <div className="action-section">
                <button 
                  type="submit" 
                  className={`seal-button ${isLoading ? 'sealing' : ''}`}
                  disabled={isLoading}
                >
                  <div className="wax-seal">
                    <div className="seal-symbol">⚔️</div>
                  </div>
                  <span className="button-text">
                    {isLoading ? "Sellando con cera..." : "Sellar en el Libro"}
                  </span>
                </button>
              </div>
            </form>
            
            <div className="page-footer">
              <div className="scribe-signature">~ Escrito por un valiente aventurero ~</div>
              <div className="page-number">Página Nueva</div>
            </div>
          </div>
        </div>
        
        {/* Divisor central del libro */}
        <div className="book-spine"></div>
      </div>
      
      {/* Botón de navegación derecho */}
      <button 
        className={`nav-arrow nav-right ${currentNoteIndex <= 0 ? 'disabled' : ''}`}
        onClick={goToNextNote}
        disabled={currentNoteIndex <= 0 || isLoading}
        title="Nota siguiente"
      >
        <span className="arrow-icon">▶</span>
      </button>
    </div>
  );
};

export default CreateNotePage;