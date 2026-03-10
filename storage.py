from addressbook import AddressBook
from notebook import NoteBook


def save_addressbook(book: AddressBook, filename: str = "addressbook.pkl") -> None:
    raise NotImplementedError("AddressBook persistence will be implemented in TASK-3.")


def load_addressbook(filename: str = "addressbook.pkl") -> AddressBook:
    raise NotImplementedError("AddressBook persistence will be implemented in TASK-3.")


def save_notebook(book: NoteBook, filename: str = "notebook.pkl") -> None:
    raise NotImplementedError("NoteBook persistence will be implemented in TASK-3.")


def load_notebook(filename: str = "notebook.pkl") -> NoteBook:
    raise NotImplementedError("NoteBook persistence will be implemented in TASK-3.")
