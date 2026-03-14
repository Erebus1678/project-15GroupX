from addressbook import AddressBook
from errors import ValidationError, input_error
from notebook import NoteBook
from services import (
    add_contact as add_contact_service,
    add_phone as add_phone_service,
    change_phone,
    create_note,
    set_address as set_address_service,
    set_birthday as set_birthday_service,
    set_email as set_email_service,
)

HELP_TEXT = """
Commands:
  Contacts:
    add <name> <phone>                - Add new contact
    add-phone <name> <phone>          - Add another phone to a contact
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

def parse_input(user_input: str) -> tuple[str, list[str]]:
    parts = user_input.strip().split()
    if not parts:
        return "", []
    command, *args = parts
    return command.lower(), args

@input_error
def add_contact(args: list[str], book: AddressBook) -> str:
    if len(args) < 2:
        raise ValidationError("Usage: add <name> <phone>")
    name, phone, *_ = args
    add_contact_service(book, name, phone)
    return "Contact added."

@input_error
def add_phone(args: list[str], book: AddressBook) -> str:
    if len(args) < 2:
        raise ValidationError("Usage: add-phone <name> <phone>")
    name, phone = args[:2]
    add_phone_service(book, name, phone)
    return "Phone added."

@input_error
def change_contact(args: list[str], book: AddressBook) -> str:
    if len(args) < 3:
        raise ValidationError("Usage: change <name> <old_phone> <new_phone>")
    name, old_phone, new_phone = args[:3]
    change_phone(book, name, old_phone, new_phone)
    return "Contact updated."

@input_error
def delete_contact(args: list[str], book: AddressBook) -> str:
    if len(args) < 1:
        raise ValidationError("Usage: delete <name>")
    name = args[0]
    book.delete(name)
    return "Contact deleted."

@input_error
def set_email(args: list[str], book: AddressBook) -> str:
    if len(args) < 2:
        raise ValidationError("Usage: set-email <name> <email>")
    name, email = args[:2]
    set_email_service(book, name, email)
    return "Email added."

@input_error
def set_address(args: list[str], book: AddressBook) -> str:
    if len(args) < 2:
        raise ValidationError("Usage: set-address <name> <address>")
    name, *address_parts = args
    set_address_service(book, name, " ".join(address_parts))
    return "Address added."

@input_error
def set_birthday(args: list[str], book: AddressBook) -> str:
    if len(args) < 2:
        raise ValidationError("Usage: set-birthday <name> <DD.MM.YYYY>")
    name, birthday = args[:2]
    set_birthday_service(book, name, birthday)
    return "Birthday added."

@input_error
def upcoming_birthdays(args: list[str], book: AddressBook) -> str:
    if len(args) < 1:
        raise ValidationError("Usage: birthdays <days>")
    if not args[0].isdigit():
        raise ValidationError("Days must be a positive integer.")
    records = book.get_upcoming_birthdays(int(args[0]))
    if not records:
        return f"No birthdays in the next {args[0]} days."
    return "\n".join(f"{r['name']}: {r['congratulation_date']}" for r in records)

@input_error
def find_contacts(args: list[str], book: AddressBook) -> str:
    if len(args) < 1:
        raise ValidationError("Usage: find <query>")
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
        raise ValidationError("Usage: add-note <text>")
    note = create_note(notebook, " ".join(args))
    return f"Note added with id: {note.note_id}."

@input_error
def edit_note(args: list[str], notebook: NoteBook) -> str:
    if len(args) < 2 or not args[0].isdigit():
        raise ValidationError("Usage: edit-note <id> <text>")
    notebook.edit(args[0], " ".join(args[1:]))
    return "Note updated."

@input_error
def delete_note(args: list[str], notebook: NoteBook) -> str:
    if not args or not args[0].isdigit():
        raise ValidationError("Usage: delete-note <id>")
    notebook.delete(args[0])
    return "Note deleted."

@input_error
def find_note(args: list[str], notebook: NoteBook) -> str:
    if len(args) < 1:
        raise ValidationError("Usage: find-note <query>")
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

def main(book: AddressBook, notebook: NoteBook) -> None:
    print("Welcome to the assistant bot!")
    print(HELP_TEXT)

    try:
        while True:
            user_input = input("\nEnter a command: ").strip()
            command, args = parse_input(user_input)

            match command:
                case "close" | "exit":
                    print("Good bye!")
                    break
                case "help":
                    print(HELP_TEXT)
                case "add":
                    print(add_contact(args, book))
                case "add-phone":
                    print(add_phone(args, book))
                case "change":
                    print(change_contact(args, book))
                case "delete":
                    print(delete_contact(args, book))
                case "set-email":
                    print(set_email(args, book))
                case "set-address":
                    print(set_address(args, book))
                case "set-birthday":
                    print(set_birthday(args, book))
                case "birthdays":
                    print(upcoming_birthdays(args, book))
                case "find":
                    print(find_contacts(args, book))
                case "all-contacts":
                    print(all_contacts(book))
                case "add-note":
                    print(add_note(args, notebook))
                case "edit-note":
                    print(edit_note(args, notebook))
                case "delete-note":
                    print(delete_note(args, notebook))
                case "find-note":
                    print(find_note(args, notebook))
                case "all-notes":
                    print(all_notes(notebook))
                case "":
                    continue
                case _:
                    print("Invalid command.")

    except (KeyboardInterrupt, EOFError):
        print("\nGood bye!")
