import { Link } from 'react-router-dom';
import type { Note } from '../../ApiService';

interface NoteCardProps {
  note: Note;
}

const NoteCard = ({ note }: NoteCardProps) => {
  const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleDateString('es-ES', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  const truncateContent = (content: string, maxLength: number = 150) => {
    if (content.length <= maxLength) return content;
    return content.substring(0, maxLength) + '...';
  };

  return (
    <div className="note-card">
      <div className="note-card-header">
        <h3 className="note-title">{note.title}</h3>
        <span className="note-date">{formatDate(note.updated_at || note.created_at)}</span>
      </div>
      
      <div className="note-content">
        <p>{truncateContent(note.content)}</p>
      </div>
      
      <div className="note-card-actions">
        <Link to={`/notes/${note.id}`} className="btn btn-secondary">
          Ver Detalles
        </Link>
        <Link to={`/notes/edit/${note.id}`} className="btn btn-outline">
          Editar
        </Link>
      </div>
    </div>
  );
};

export default NoteCard;