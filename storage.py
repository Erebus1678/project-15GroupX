from addressbook import AddressBook
from notebook import NoteBook
import pickle


def save_addressbook(book: AddressBook, filename: str = "addressbook.pkl") -> None:
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_addressbook(filename: str = "addressbook.pkl") -> AddressBook:
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()


def save_notebook(book: NoteBook, filename: str = "notebook.pkl") -> None:
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_notebook(filename: str = "notebook.pkl") -> NoteBook:
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return NoteBook()

