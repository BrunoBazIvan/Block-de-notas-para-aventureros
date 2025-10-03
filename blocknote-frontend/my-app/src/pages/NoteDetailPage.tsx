import { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { ApiService } from '../ApiService';
import type { Note } from '../ApiService';

const NoteDetailPage = () => {
  const { id } = useParams<{ id: string }>();
  const [note, setNote] = useState<Note | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchNote = async () => {
      if (!id) return;
      
      try {
        const response = await ApiService.getNoteById(Number(id));
        setNote(response.data);
      } catch (err) {
        setError('Error al cargar la nota');
        console.error('Error fetching note:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchNote();
  }, [id]);

  if (loading) return <div className="loading">Cargando nota...</div>;
  if (error) return <div className="error">{error}</div>;
  if (!note) return <div className="error">Nota no encontrada</div>;

  return (
    <div className="note-detail-page">
      <header className="page-header">
        <Link to="/notes" className="btn btn-secondary">← Volver a Notas</Link>
        <div className="header-actions">
          <Link to={`/notes/edit/${note.id}`} className="btn btn-primary">
            Editar
          </Link>
        </div>
      </header>
      
      <main className="note-detail">
        <h1 className="note-title">{note.title}</h1>
        <div className="note-meta">
          <span>Creado: {new Date(note.created_at).toLocaleDateString('es-ES')}</span>
          <span>Actualizado: {note.updated_at ? new Date(note.updated_at).toLocaleDateString('es-ES') : 'No actualizada'}</span>
        </div>
        <div className="note-content">
          <pre>{note.content}</pre>
        </div>
      </main>
    </div>
  );
};

export default NoteDetailPage;