from collections.abc import Callable
from dataclasses import dataclass

from errors import input_error
from addressbook import AddressBook, Record
from notebook import NoteBook, Note

HELP_TEXT = """
Commands:
  Contacts:
    add <name> <phone>                - Add new contact
    change <name> <old> <new>         - Change phone number
    delete <name>                     - Delete contact
    set-email <name> <email>          - Set email
    set-address <name> <address>      - Set address
    set-birthday <name> DD.MM.YYYY    - Set birthday
    birthdays <days>                  - Contacts with birthday in N days
    find <query>                      - Search by name / phone / email
    all-contacts                      - Show all contacts

  Notes:
    add-note <text>                   - Add note
    edit-note <id> <text>             - Edit note text
    delete-note <id>                  - Delete note
    find-note <query>                 - Search notes by text
    all-notes                         - Show all notes

  General:
    help                              - Show this menu
    close / exit                      - Save and exit
""".strip()

SAVE_ON_SUCCESS = {
    "Contact added.",
    "Contact updated.",
    "Contact deleted.",
    "Email added.",
    "Address added.",
    "Birthday added.",
    "Note updated.",
    "Note deleted.",
}


@dataclass(frozen=True)
class CommandSpec:
    handler: Callable[[list[str]], str]
    mutates: bool = False


def parse_input(user_input: str) -> tuple[str, list[str]]:
    parts = user_input.strip().split()
    if not parts:
        return "", []
    command, *args = parts
    return command.lower(), args


def save_after_success(message: str, save_state: Callable[[], None]) -> str:
    if message in SAVE_ON_SUCCESS or message.startswith("Note added with id: "):
        save_state()
    return message


def show_help(_: list[str]) -> str:
    return HELP_TEXT


@input_error
def add_contact(args: list[str], book: AddressBook) -> str:
    if len(args) < 2:
        raise ValueError("Usage: add <name> <phone>")
    name, phone, *_ = args
    record = Record(name)
    record.add_phone(phone)
    book.add_record(record)
    return "Contact added."


@input_error
def change_contact(args: list[str], book: AddressBook) -> str:
    if len(args) < 3:
        raise ValueError("Usage: change <name> <old_phone> <new_phone>")
    name, old_phone, new_phone = args[:3]
    record = book.find(name)
    if record is None:
        raise KeyError("Contact not found.")
    record.edit_phone(old_phone, new_phone)
    return "Contact updated."


@input_error
def delete_contact(args: list[str], book: AddressBook) -> str:
    if len(args) < 1:
        raise ValueError("Usage: delete <name>")
    name = args[0]
    book.delete(name)
    return "Contact deleted."


@input_error
def set_email(args: list[str], book: AddressBook) -> str:
    if len(args) < 2:
        raise ValueError("Usage: set-email <name> <email>")
    name, email = args[:2]
    record = book.find(name)
    if record is None:
        raise KeyError("Contact not found.")
    record.set_email(email)
    return "Email added."


@input_error
def set_address(args: list[str], book: AddressBook) -> str:
    if len(args) < 2:
        raise ValueError("Usage: set-address <name> <address>")
    name, *address_parts = args
    record = book.find(name)
    if record is None:
        raise KeyError("Contact not found.")
    record.set_address(" ".join(address_parts))
    return "Address added."


@input_error
def set_birthday(args: list[str], book: AddressBook) -> str:
    if len(args) < 2:
        raise ValueError("Usage: set-birthday <name> <DD.MM.YYYY>")
    name, birthday = args[:2]
    record = book.find(name)
    if record is None:
        raise KeyError("Contact not found.")
    record.add_birthday(birthday)
    return "Birthday added."


@input_error
def upcoming_birthdays(args: list[str], book: AddressBook) -> str:
    if len(args) < 1:
        raise ValueError("Usage: birthdays <days>")
    if not args[0].isdigit():
        raise ValueError("Days must be a positive integer.")
    records = book.get_upcoming_birthdays(int(args[0]))
    if not records:
        return f"No birthdays in the next {args[0]} days."
    return "\n".join(f"{r['name']}: {r['congratulation_date']}" for r in records)


@input_error
def find_contacts(args: list[str], book: AddressBook) -> str:
    if len(args) < 1:
        raise ValueError("Usage: find <query>")
    results = book.search(" ".join(args))
    if not results:
        return "No contacts found."
    return "\n".join(str(r) for r in results)


@input_error
def all_contacts(book: AddressBook) -> str:
    if not book.data:
        return "No contacts saved."
    return "\n".join(str(record) for record in book.data.values())


@input_error
def add_note(args: list[str], notebook: NoteBook) -> str:
    if len(args) < 1:
        raise ValueError("Usage: add-note <text>")

    text = " ".join(args).strip()
    if not text:
        raise ValueError("Note text cannot be empty.")

    numeric_note_ids = [int(note_id) for note_id in notebook.data if str(note_id).isdigit()]
    next_note_id = max(numeric_note_ids, default=0) + 1

    note = Note(str(next_note_id), text)
    notebook.add_note(note)
    return f"Note added with id: {next_note_id}."


@input_error
def edit_note(args: list[str], notebook: NoteBook) -> str:
    if len(args) < 2 or not args[0].isdigit():
        raise ValueError("Usage: edit-note <id> <text>")

    note_id = args[0]
    new_text = " ".join(args[1:]).strip()
    if not new_text:
        raise ValueError("Note text cannot be empty.")

    notebook.edit(note_id, new_text)
    return "Note updated."


@input_error
def delete_note(args: list[str], notebook: NoteBook) -> str:
    if not args or not args[0].isdigit():
        raise ValueError("Usage: delete-note <id>")
    notebook.delete(args[0])
    return "Note deleted."


@input_error
def find_note(args: list[str], notebook: NoteBook) -> str:
    if len(args) < 1:
        raise ValueError("Usage: find-note <query>")
    results = notebook.find(" ".join(args))
    if not results:
        return "No notes found."
    return "\n".join(str(n) for n in results)


@input_error
def all_notes(notebook: NoteBook) -> str:
    notes = notebook.list_notes()
    if not notes:
        return "No notes saved."
    return "\n".join(str(note) for note in notes)


def main(book: AddressBook, notebook: NoteBook, save_state: Callable[[], None]) -> None:
    commands = {
        "help": CommandSpec(show_help),
        "add": CommandSpec(lambda args: add_contact(args, book), mutates=True),
        "change": CommandSpec(lambda args: change_contact(args, book), mutates=True),
        "delete": CommandSpec(lambda args: delete_contact(args, book), mutates=True),
        "set-email": CommandSpec(lambda args: set_email(args, book), mutates=True),
        "set-address": CommandSpec(lambda args: set_address(args, book), mutates=True),
        "set-birthday": CommandSpec(lambda args: set_birthday(args, book), mutates=True),
        "birthdays": CommandSpec(lambda args: upcoming_birthdays(args, book)),
        "find": CommandSpec(lambda args: find_contacts(args, book)),
        "all-contacts": CommandSpec(lambda _: all_contacts(book)),
        "add-note": CommandSpec(lambda args: add_note(args, notebook), mutates=True),
        "edit-note": CommandSpec(lambda args: edit_note(args, notebook), mutates=True),
        "delete-note": CommandSpec(lambda args: delete_note(args, notebook), mutates=True),
        "find-note": CommandSpec(lambda args: find_note(args, notebook)),
        "all-notes": CommandSpec(lambda _: all_notes(notebook)),
    }
    exit_commands = {"close", "exit"}

    print("Welcome to the assistant bot!")
    print(HELP_TEXT)

    try:
        while True:
            user_input = input("\nEnter a command: ").strip()
            command, args = parse_input(user_input)

            if command in exit_commands:
                print("Good bye!")
                break
            if command == "":
                continue
            command_spec = commands.get(command)
            if command_spec is None:
                print("Invalid command.")
                continue

            response = command_spec.handler(args)
            if command_spec.mutates:
                response = save_after_success(response, save_state)
            print(response)

    except (KeyboardInterrupt, EOFError):
        print("\nGood bye!")
