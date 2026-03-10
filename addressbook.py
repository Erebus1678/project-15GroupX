from collections import UserDict
from typing import Optional


class Field:
    """Base class for contact fields."""

    def __init__(self, value: str):
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Name(Field):
    """Contact name field."""


class Address(Field):
    """Contact address field."""


class Phone(Field):
    """Phone field. Validation will be implemented in TASK-1."""


class Email(Field):
    """Email field. Validation will be implemented in TASK-1."""


class Birthday(Field):
    """Birthday field. Validation will be implemented in TASK-1."""


class Record:
    """Single contact record."""

    def __init__(self, name: str):
        self.name = Name(name.strip())
        self.address: Optional[Address] = None
        self.phones: list[Phone] = []
        self.email: Optional[Email] = None
        self.birthday: Optional[Birthday] = None

    def set_address(self, address: str) -> None:
        raise NotImplementedError("Address handling will be implemented in TASK-1.")

    def set_email(self, email: str) -> None:
        raise NotImplementedError("Email handling will be implemented in TASK-1.")

    def add_phone(self, phone: str) -> None:
        raise NotImplementedError("Phone handling will be implemented in TASK-1.")

    def remove_phone(self, phone: str) -> None:
        raise NotImplementedError("Phone removal will be implemented in TASK-1.")

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        raise NotImplementedError("Phone editing will be implemented in TASK-1.")

    def find_phone(self, phone: str) -> Optional[Phone]:
        raise NotImplementedError("Phone lookup will be implemented in TASK-1.")

    def add_birthday(self, birthday: str) -> None:
        raise NotImplementedError("Birthday handling will be implemented in TASK-1.")

    def __str__(self) -> str:
        raise NotImplementedError("Record string formatting will be implemented in TASK-1.")


class AddressBook(UserDict):
    """Collection of contact records."""

    def add_record(self, record: Record) -> None:
        raise NotImplementedError("Record storage will be implemented in TASK-1.")

    def find(self, name: str) -> Optional[Record]:
        raise NotImplementedError("Record lookup will be implemented in TASK-1.")

    def delete(self, name: str) -> None:
        raise NotImplementedError("Record deletion will be implemented in TASK-1.")

    def search(self, query: str) -> list[Record]:
        raise NotImplementedError("Record search will be implemented in TASK-1.")

    def get_upcoming_birthdays(self, days: int = 7) -> list[dict[str, str]]:
        raise NotImplementedError("Birthday reporting will be implemented in TASK-1.")
