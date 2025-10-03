import { ApiService } from "../ApiService";
import { useState } from "react";

const CreateNotePage = () => {
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const handleCreateNote = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!title.trim() || !content.trim()) {
      alert("Por favor, completa todos los campos");
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
      
      alert("Nota creada exitosamente!");
    } catch (error) {
      console.error("Error al crear la nota:", error);
      alert("Error al crear la nota. Inténtalo de nuevo.");
    } finally {
      setIsLoading(false);
    }
  };
  
  return (
    <div className="create-note-page">
      <h1>Crear Nueva Nota</h1>
      <form onSubmit={handleCreateNote}>
        <input 
          type="text" 
          placeholder="Título de la nota"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          disabled={isLoading}
          required
        />
        <textarea 
          placeholder="Contenido de la nota"
          value={content}
          onChange={(e) => setContent(e.target.value)}
          disabled={isLoading}
          required
        />
        <button 
          type="submit" 
          className="btn btn-primary"
          disabled={isLoading}
        >
          {isLoading ? "Guardando..." : "Guardar Nota"}
        </button>
      </form>
    </div>
  );
};

export default CreateNotePage;