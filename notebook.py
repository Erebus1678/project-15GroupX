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


if __name__ == "__main__":
    # Simple manual demo for quick testing
    notebook = NoteBook()

    # 1. Add notes
    note1 = Note("1", "Buy milk")
    note2 = Note("2", "Prepare for the exam")
    notebook.add_note(note1)
    notebook.add_note(note2)

    print("=== All notes after adding ===")
    for note in notebook.list_notes():
        print(note)

    # 2. Find by text
    print("\n=== Search by word 'milk' ===")
    for note in notebook.find("milk"):
        print(note)

    # 3. Edit a note
    print("\n=== Edit note with id '1' ===")
    notebook.edit("1", "Buy milk and bread")
    print(notebook.data["1"])

    # 4. Delete a note
    print("\n=== Delete note with id '2' ===")
    notebook.delete("2")
    print("Remaining notes:")
    for note in notebook.list_notes():
        print(note)


"""
==================== Note and NoteBook module documentation ====================

Classes
-------

1) Note
   - Purpose: represents a single text note.
   - Fields:
       note_id (str) — unique note identifier;
       text (str) — note text.
   - Methods:
       edit(new_text: str) -> None
           Update note text.
       __str__() -> str
           Return string representation: "<note_id>: <text>".

2) NoteBook (inherits from UserDict)
   - Purpose: collection of notes stored separately from contacts.
   - Internal storage:
       self.data — dict where key is note_id and value is a Note instance.

   Methods:
   - add_note(note: Note) -> None
       Add a new note to the notebook.
       The key is note.note_id.
       Raises ValueError if a note with the given id already exists.

   - find(query: str) -> list[Note]
       Return a list of notes whose text contains the given query
       (case-insensitive search).

   - edit(note_id: str, new_text: str) -> None
       Edit note text by its id.
       Raises ValueError if a note with the given id does not exist.

   - delete(note_id: str) -> None
       Delete a note by its id.
       Raises ValueError if a note with the given id does not exist.

   - list_notes() -> list[Note]
       Return a list of all notes.

Usage example
-------------

from notebook import Note, NoteBook

notebook = NoteBook()

# Add notes
note1 = Note("1", "Buy milk")
note2 = Note("2", "Prepare for the exam")
notebook.add_note(note1)
notebook.add_note(note2)

# Print all notes
for note in notebook.list_notes():
    print(note)

# Search notes
results = notebook.find("milk")
for note in results:
    print("Found:", note)

# Edit a note
notebook.edit("1", "Buy milk and bread")

# Delete a note
notebook.delete("2")

CLI integration
---------------

The NoteBook class can be used in the command-line interface
of the personal assistant. Typical commands based on this module:

- add-note: create a new note, asking user for the text;
- list-notes: show all notes;
- edit-note: change note text by id;
- delete-note: delete a note by id;
- find-notes: search notes by a query string.

This module satisfies TASK-2 requirements:
adding, searching, editing and deleting notes.
"""
