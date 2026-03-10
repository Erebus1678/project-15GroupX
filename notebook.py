from collections import UserDict
from typing import Optional


class Note:
    """Single note entity."""

    def __init__(self, note_id: str, text: str):
        self.note_id = note_id
        self.text = text

    def edit(self, new_text: str) -> None:
        raise NotImplementedError("Note editing will be implemented in TASK-2.")

    def __str__(self) -> str:
        return f"{self.note_id}: {self.text}"


class NoteBook(UserDict):
    """Collection of notes stored separately from contacts."""

    def add_note(self, note: Note) -> None:
        raise NotImplementedError("Note storage will be implemented in TASK-2.")

    def find(self, query: str) -> list[Note]:
        raise NotImplementedError("Note search will be implemented in TASK-2.")

    def edit(self, note_id: str, new_text: str) -> None:
        raise NotImplementedError("Note editing will be implemented in TASK-2.")

    def delete(self, note_id: str) -> None:
        raise NotImplementedError("Note deletion will be implemented in TASK-2.")

    def list_notes(self) -> list[Note]:
        raise NotImplementedError("Listing notes will be implemented in TASK-2.")
