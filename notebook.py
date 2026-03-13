from collections import UserDict
from typing import Optional


class Note:
    """Single note entity."""

    def __init__(self, note_id: str, text: str):
        self.note_id = note_id
        self.text = text

    def edit(self, new_text: str) -> None:
        """Update note text."""
        self.text = new_text

    def __str__(self) -> str:
        return f"{self.note_id}: {self.text}"


class NoteBook(UserDict):
    """Collection of notes stored separately from contacts."""

    def add_note(self, note: Note) -> None:
        """
        Add a new note to the notebook.

        The key is note.note_id.
        Raises ValueError if a note with the given id already exists.
        """
        if note.note_id in self.data:
            raise ValueError(f"Note with id {note.note_id} already exists.")
        self.data[note.note_id] = note

    def find(self, query: str) -> list[Note]:
        """
        Return a list of notes whose text contains the given query
        (case-insensitive search).
        """
        q = query.lower()
        return [note for note in self.data.values() if q in note.text.lower()]

    def edit(self, note_id: str, new_text: str) -> None:
        """
        Edit note text by its id.

        Raises ValueError if a note with the given id does not exist.
        """
        note: Optional[Note] = self.data.get(note_id)
        if note is None:
            raise ValueError(f"Note with id {note_id} not found.")
        note.edit(new_text)

    def delete(self, note_id: str) -> None:
        """
        Delete a note by its id.

        Raises ValueError if a note with the given id does not exist.
        """
        if note_id not in self.data:
            raise ValueError(f"Note with id {note_id} not found.")
        del self.data[note_id]

    def list_notes(self) -> list[Note]:
        """Return a list of all notes."""
        return list(self.data.values())
