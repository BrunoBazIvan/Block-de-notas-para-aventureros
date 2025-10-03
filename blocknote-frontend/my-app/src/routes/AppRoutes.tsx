import { Routes, Route } from 'react-router-dom';
import NotesListPage from '../pages/NotesListPage';
import NoteDetailPage from '../pages/NoteDetailPage';
import CreateNotePage from '../pages/CreateNotePage';
import EditNotePage from '../pages/EditNotePage';

const AppRoutes = () => {
  return (
    <Routes>
      <Route path="/" element={<NotesListPage />} />
      <Route path="/notes" element={<NotesListPage />} />
      <Route path="/notes/:id" element={<NoteDetailPage />} />
      <Route path="/notes/create" element={<CreateNotePage />} />
      <Route path="/notes/edit/:id" element={<EditNotePage />} />
    </Routes>
  );
};

export default AppRoutes;