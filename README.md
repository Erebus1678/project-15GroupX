# Personal Assistant

`Personal Assistant` is a command-line Python application for managing contacts and notes with persistent local storage.

## Features

- add, edit, search, and delete contacts
- store contact phones, email, address, and birthday
- validate phone numbers and email addresses during input
- show upcoming birthdays for the next N days
- add, edit, search, and delete notes
- keep data between runs using pickle storage

## Requirements

- Python 3.10 or newer

## Installation

Clone the repository and move into the project directory:

```bash
git clone https://github.com/Erebus1678/project-15GroupX.git
cd project-15GroupX
```

Optionally create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS / Linux:

```bash
source .venv/bin/activate
```

The project uses only the Python standard library, so no extra packages are required.

## Project Structure

```text
main.py
cli.py
addressbook.py
notebook.py
storage.py
errors.py
README.md
```

## Module Roles

- `main.py` - application entry point and save/load lifecycle
- `cli.py` - command loop, parsing, and user interaction
- `addressbook.py` - contact entities, validation, search, and birthdays
- `notebook.py` - note entities and notebook operations
- `storage.py` - pickle-based persistence helpers
- `errors.py` - shared CLI error handling decorator

## Run

```bash
python main.py
```

After launch, the assistant prints the available commands and keeps running until you enter `close` or `exit`.

## Quick Start

Minimal example:

```text
add John 1234567890
set-email John john@example.com
set-address John 12 Green Street
set-birthday John 15.08.1995
add-note Buy milk after work
all-contacts
all-notes
exit
```

## Available Commands

### Contacts

- `add <name> <phone>` - create a new contact with the first phone number
- `change <name> <old_phone> <new_phone>` - replace an existing phone number
- `delete <name>` - remove a contact from the address book
- `set-email <name> <email>` - assign or update email
- `set-address <name> <address>` - assign or update address
- `set-birthday <name> <DD.MM.YYYY>` - save birthday in day-month-year format
- `birthdays <days>` - show contacts with birthdays in the next N days
- `find <query>` - search by name, phone, email, address, or birthday text
- `all-contacts` - print all saved contacts

### Notes

- `add-note <text>` - create a note with an auto-generated numeric id
- `edit-note <id> <text>` - update note content
- `delete-note <id>` - remove a note
- `find-note <query>` - search note text
- `all-notes` - print all saved notes

### General

- `help` - print the command list
- `close` - save data and close the program
- `exit` - save data and close the program

## Storage

By default, the application stores data in the user home directory:

- `~/.personal_assistant/addressbook.pkl`
- `~/.personal_assistant/notebook.pkl`

This allows contacts and notes to remain available after restarting the program.

The application saves data:

- after successful changes to contacts and notes;
- when the program exits normally;
- when the session is interrupted with `Ctrl+C` or `Ctrl+D`.

## Validation and Error Handling

- Phone numbers must contain exactly 10 digits.
- Email addresses are validated before saving.
- Birthdays must use the `DD.MM.YYYY` format.
- Invalid commands or invalid data do not crash the application; the CLI shows an error message and continues running.

## Notes on Behavior

- The help menu is printed once on startup and can be shown again with `help`.
- Birthday output is calculated relative to the current date.
- If a birthday falls on a weekend, the congratulation date is moved to the next Monday.
- Notes receive incremental numeric ids starting from `1`.

## Example Session

```text
add John 1234567890
set-email John john@example.com
set-address John 12 Green Street
set-birthday John 15.08.1995
add-note Buy milk after work
find John
all-notes
exit
```
