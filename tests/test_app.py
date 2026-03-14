import unittest

from addressbook import AddressBook
from cli import add_note, add_phone
from errors import NoteNotFoundError
from notebook import Note, NoteBook
from services import add_contact


class ContactCliTests(unittest.TestCase):
    def test_add_phone_adds_second_phone_to_existing_contact(self) -> None:
        book = AddressBook()
        add_contact(book, "John", "1234567890")

        result = add_phone(["John", "0987654321"], book)

        self.assertEqual(result, "Phone added.")
        self.assertEqual(
            [phone.value for phone in book.find("John").phones],
            ["1234567890", "0987654321"],
        )


class NoteBookTests(unittest.TestCase):
    def test_create_note_uses_next_numeric_id(self) -> None:
        notebook = NoteBook()
        notebook.add_note(Note("3", "Existing"))

        note = notebook.create_note("  New note  ")

        self.assertEqual(note.note_id, "4")
        self.assertEqual(note.text, "New note")

    def test_edit_missing_note_raises_domain_error(self) -> None:
        notebook = NoteBook()

        with self.assertRaises(NoteNotFoundError):
            notebook.edit("1", "Updated")


class NoteCliTests(unittest.TestCase):
    def test_add_note_returns_generated_id(self) -> None:
        notebook = NoteBook()

        result = add_note(["Buy", "milk"], notebook)

        self.assertEqual(result, "Note added with id: 1.")
        self.assertIn("1", notebook.data)


if __name__ == "__main__":
    unittest.main()
