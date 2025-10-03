const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8080/api';

// Tipos TypeScript para las notas
export interface Note {
  id: number;
  title: string;
  content: string;
  created_at: string;
  updated_at: string | null;
}

export interface NoteCreate {
  title: string;
  content: string;
}

export interface NoteUpdate {
  title?: string;
  content?: string;
}

export const ApiService = {
  // Obtener todas las notas
  getAllNotes: async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/notes`);
      if (!response.ok) {
        throw new Error('Error al obtener las notas');
      }
      const data = await response.json();
      return { data };
    } catch (error) {
      console.error('Error in getAllNotes:', error);
      throw error;
    }
  },

  // Obtener una nota por ID
  getNoteById: async (id: number) => {
    try {
      const response = await fetch(`${API_BASE_URL}/notes/${id}`);
      if (!response.ok) {
        throw new Error('Error al obtener la nota');
      }
      const data = await response.json();
      return { data };
    } catch (error) {
      console.error('Error in getNoteById:', error);
      throw error;
    }
  },

  // Crear una nueva nota
  createNote: async (noteData: { title: string; content: string }) => {
    try {
      const response = await fetch(`${API_BASE_URL}/notes`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(noteData),
      });
      if (!response.ok) {
        throw new Error('Error al crear la nota');
      }
      const data = await response.json();
      return { data };
    } catch (error) {
      console.error('Error in createNote:', error);
      throw error;
    }
  },

  // Actualizar una nota
  updateNote: async (id: number, noteData: { title: string; content: string }) => {
    try {
      const response = await fetch(`${API_BASE_URL}/notes/${id}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(noteData),
      });
      if (!response.ok) {
        throw new Error('Error al actualizar la nota');
      }
      const data = await response.json();
      return { data };
    } catch (error) {
      console.error('Error in updateNote:', error);
      throw error;
    }
  },

  // Eliminar una nota
  deleteNote: async (id: number) => {
    try {
      const response = await fetch(`${API_BASE_URL}/notes/${id}`, {
        method: 'DELETE',
      });
      if (!response.ok) {
        throw new Error('Error al eliminar la nota');
      }
      return { success: true };
    } catch (error) {
      console.error('Error in deleteNote:', error);
      throw error;
    }
  },
};
