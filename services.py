from addressbook import AddressBook, Record
from errors import ContactNotFoundError
from notebook import NoteBook


def _get_record(book: AddressBook, name: str) -> Record:
    record = book.find(name)
    if record is None:
        raise ContactNotFoundError("Contact not found.")
    return record


def add_contact(book: AddressBook, name: str, phone: str) -> None:
    record = Record(name)
    record.add_phone(phone)
    book.add_record(record)


def add_phone(book: AddressBook, name: str, phone: str) -> None:
    _get_record(book, name).add_phone(phone)


def change_phone(book: AddressBook, name: str, old_phone: str, new_phone: str) -> None:
    _get_record(book, name).edit_phone(old_phone, new_phone)


def set_email(book: AddressBook, name: str, email: str) -> None:
    _get_record(book, name).set_email(email)


def set_address(book: AddressBook, name: str, address: str) -> None:
    _get_record(book, name).set_address(address)


def set_birthday(book: AddressBook, name: str, birthday: str) -> None:
    _get_record(book, name).add_birthday(birthday)


def create_note(notebook: NoteBook, text: str):
    return notebook.create_note(text)
