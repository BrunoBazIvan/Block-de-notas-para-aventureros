import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import NoteCard from '../components/notes/NoteCard';
import { ApiService } from '../ApiService';
import type { Note } from '../ApiService';

const NotesListPage = () => {
  const [notes, setNotes] = useState<Note[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchNotes = async () => {
      try {
        const response = await ApiService.getAllNotes();
        setNotes(response.data || []);
      } catch (err) {
        setError('Error al cargar las notas');
        console.error('Error fetching notes:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchNotes();
  }, []);

  if (loading) return <div className="loading">Cargando notas...</div>;
  if (error) return <div className="error">{error}</div>;

  return (
    <div className="notes-list-page">
      <header className="page-header">
        <h1>Mis Notas Aventureras</h1>
        <Link to="/notes/create" className="btn btn-primary">
          Crear Nueva Nota
        </Link>
      </header>
      
      <main className="notes-grid">
        {notes.length === 0 ? (
          <div className="empty-state">
            <h3>No tienes notas aún</h3>
            <p>¡Comienza tu aventura creando tu primera nota!</p>
            <Link to="/notes/create" className="btn btn-primary">
              Crear Primera Nota
            </Link>
          </div>
        ) : (
          notes.map((note) => (
            <NoteCard key={note.id} note={note} />
          ))
        )}
      </main>
    </div>
  );
};

export default NotesListPage;