from addressbook import AddressBook
from notebook import NoteBook
import pickle
from pathlib import Path
from typing import Callable, TypeVar


T = TypeVar("T")
DATA_DIR = Path.home() / ".personal_assistant"
ADDRESSBOOK_FILE = DATA_DIR / "addressbook.pkl"
NOTEBOOK_FILE = DATA_DIR / "notebook.pkl"


def _resolve_path(filename: str | Path | None, default_path: Path) -> Path:
    return Path(filename) if filename is not None else default_path


def _save_data(data: object, filename: str | Path | None, default_path: Path) -> None:
    path = _resolve_path(filename, default_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as file:
        pickle.dump(data, file)


def _load_data(
    filename: str | Path | None, default_path: Path, factory: Callable[[], T]
) -> T:
    path = _resolve_path(filename, default_path)
    try:
        with path.open("rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return factory()


def save_addressbook(book: AddressBook, filename: str | Path | None = None) -> None:
    _save_data(book, filename, ADDRESSBOOK_FILE)


def load_addressbook(filename: str | Path | None = None) -> AddressBook:
    return _load_data(filename, ADDRESSBOOK_FILE, AddressBook)


def save_notebook(book: NoteBook, filename: str | Path | None = None) -> None:
    _save_data(book, filename, NOTEBOOK_FILE)


def load_notebook(filename: str | Path | None = None) -> NoteBook:
    return _load_data(filename, NOTEBOOK_FILE, NoteBook)

