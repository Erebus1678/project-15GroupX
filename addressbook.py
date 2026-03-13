import re
from collections import UserDict
from datetime import date, datetime, timedelta
from typing import Optional


class Field:
    """Base class for contact fields."""

    def __init__(self, value: str):
        self.value = value

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, value: str) -> None:
        self._value = value

    def __str__(self) -> str:
        return str(self.value)


class Name(Field):
    """Contact name field."""

    @Field.value.setter
    def value(self, value: str) -> None:
        cleaned_value = value.strip()
        if not cleaned_value:
            raise ValueError("Name cannot be empty.")
        self._value = cleaned_value


class Address(Field):
    """Contact address field."""

    @Field.value.setter
    def value(self, value: str) -> None:
        cleaned_value = value.strip()
        if not cleaned_value:
            raise ValueError("Address cannot be empty.")
        self._value = cleaned_value


class Phone(Field):
    """Phone field with 10-digit validation."""

    @Field.value.setter
    def value(self, value: str) -> None:
        cleaned_value = value.strip()
        if not (cleaned_value.isdigit() and len(cleaned_value) == 10):
            raise ValueError("Invalid phone number. Phone must contain 10 digits.")
        self._value = cleaned_value


class Email(Field):
    """Email field with basic format validation."""

    EMAIL_PATTERN = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

    @Field.value.setter
    def value(self, value: str) -> None:
        cleaned_value = value.strip()
        if not self.EMAIL_PATTERN.fullmatch(cleaned_value):
            raise ValueError("Invalid email format.")
        self._value = cleaned_value


class Birthday(Field):
    """Birthday field with DD.MM.YYYY validation."""

    def __init__(self, value: str):
        self.value = value

    @property
    def value(self) -> date:
        return self._value

    @value.setter
    def value(self, value: str) -> None:
        cleaned_value = value.strip()
        try:
            parsed_date = datetime.strptime(cleaned_value, "%d.%m.%Y").date()
        except ValueError as error:
            raise ValueError("Invalid date format. Use DD.MM.YYYY") from error
        self._value = parsed_date

    def __str__(self) -> str:
        return self.value.strftime("%d.%m.%Y")


class Record:
    """Single contact record."""

    def __init__(self, name: str):
        self.name = Name(name)
        self.address: Optional[Address] = None
        self.phones: list[Phone] = []
        self.email: Optional[Email] = None
        self.birthday: Optional[Birthday] = None

    def set_address(self, address: str) -> None:
        self.address = Address(address)

    def set_email(self, email: str) -> None:
        self.email = Email(email)

    def add_phone(self, phone: str) -> None:
        new_phone = Phone(phone)
        if self.find_phone(new_phone.value) is not None:
            raise ValueError("Phone number already exists.")
        self.phones.append(new_phone)

    def remove_phone(self, phone: str) -> None:
        existing_phone = self.find_phone(phone)
        if existing_phone is None:
            raise ValueError("Phone number not found.")
        self.phones.remove(existing_phone)

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        current_phone = self.find_phone(old_phone)
        if current_phone is None:
            raise ValueError("Old phone number not found.")

        replacement_phone = Phone(new_phone)
        if replacement_phone.value != current_phone.value and self.find_phone(replacement_phone.value) is not None:
            raise ValueError("Phone number already exists.")

        current_phone.value = replacement_phone.value

    def find_phone(self, phone: str) -> Optional[Phone]:
        cleaned_phone = phone.strip()
        for existing_phone in self.phones:
            if existing_phone.value == cleaned_phone:
                return existing_phone
        return None

    def add_birthday(self, birthday: str) -> None:
        self.birthday = Birthday(birthday)

    def matches(self, query: str) -> bool:
        cleaned_query = query.strip().lower()
        if not cleaned_query:
            return True

        searchable_values = [
            self.name.value.lower(),
            self.address.value.lower() if self.address else "",
            self.email.value.lower() if self.email else "",
            str(self.birthday).lower() if self.birthday else "",
        ]
        searchable_values.extend(phone.value.lower() for phone in self.phones)
        return any(cleaned_query in value for value in searchable_values)

    def __str__(self) -> str:
        address_value = self.address.value if self.address else "not set"
        phones_value = ", ".join(phone.value for phone in self.phones) if self.phones else "not set"
        email_value = self.email.value if self.email else "not set"
        birthday_value = str(self.birthday) if self.birthday else "not set"
        return (
            f"{self.name.value}: "
            f"address: {address_value}; "
            f"phones: {phones_value}; "
            f"email: {email_value}; "
            f"birthday: {birthday_value}"
        )


class AddressBook(UserDict):
    """Collection of contact records."""

    @staticmethod
    def _birthday_for_year(birthday: date, year: int) -> date:
        try:
            return birthday.replace(year=year)
        except ValueError:
            return date(year, 3, 1)

    def add_record(self, record: Record) -> None:
        if record.name.value in self.data:
            raise ValueError("Contact already exists.")
        self.data[record.name.value] = record

    def find(self, name: str) -> Optional[Record]:
        return self.data.get(name.strip())

    def delete(self, name: str) -> None:
        cleaned_name = name.strip()
        if cleaned_name not in self.data:
            raise KeyError("Contact not found.")
        del self.data[cleaned_name]

    def search(self, query: str) -> list[Record]:
        return [record for record in self.data.values() if record.matches(query)]

    def get_upcoming_birthdays(self, days: int = 7) -> list[dict[str, str]]:
        if days < 0:
            raise ValueError("Days must be zero or greater.")

        today = date.today()
        end_date = today + timedelta(days=days)
        upcoming_birthdays: list[dict[str, str]] = []

        for record in self.data.values():
            if record.birthday is None:
                continue

            birthday_date = record.birthday.value
            birthday_this_year = self._birthday_for_year(birthday_date, today.year)

            if birthday_this_year < today:
                birthday_this_year = self._birthday_for_year(birthday_date, today.year + 1)

            if today <= birthday_this_year <= end_date:
                congratulation_date = birthday_this_year
                if congratulation_date.weekday() == 5:
                    congratulation_date += timedelta(days=2)
                elif congratulation_date.weekday() == 6:
                    congratulation_date += timedelta(days=1)

                upcoming_birthdays.append(
                    {
                        "name": record.name.value,
                        "congratulation_date": congratulation_date.strftime("%d.%m.%Y"),
                    }
                )

        upcoming_birthdays.sort(
            key=lambda item: (
                datetime.strptime(item["congratulation_date"], "%d.%m.%Y").date(),
                item["name"].lower(),
            )
        )
        return upcoming_birthdays
