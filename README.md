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

## Install

Install the project as a package from the repository root:

```bash
python -m pip install .
```

For local development, you can use editable mode:

```bash
python -m pip install -e .
```

## Project Structure

```text
pyproject.toml
main.py
cli.py
addressbook.py
notebook.py
services.py
storage.py
errors.py
README.md
```

## Module Roles

- `main.py` - application entry point and save/load lifecycle
- `cli.py` - command loop, parsing, and user interaction
- `addressbook.py` - contact entities, validation, search, and birthdays
- `notebook.py` - note entities and notebook operations
- `services.py` - application-level contact and note operations used by CLI
- `storage.py` - pickle-based persistence helpers
- `errors.py` - shared CLI error handling decorator

## Run

After installation, launch the assistant from any directory with:

```bash
personal-assistant
```

You can also run it directly from the project root during development:

```bash
python main.py
```

After launch, the assistant prints the available commands and keeps running until you enter `close` or `exit`.

## Available Commands

### Contacts

- `add <name> <phone>`
- `add-phone <name> <phone>`
- `change <name> <old_phone> <new_phone>`
- `delete <name>`
- `set-email <name> <email>`
- `set-address <name> <address>`
- `set-birthday <name> <DD.MM.YYYY>`
- `birthdays <days>`
- `find <query>`
- `all-contacts`

### Notes

- `add-note <text>`
- `edit-note <id> <text>`
- `delete-note <id>`
- `find-note <query>`
- `all-notes`

### General

- `help`
- `close`
- `exit`

## Storage

By default, the application stores data in the user home directory:

- `~/.personal_assistant/addressbook.pkl`
- `~/.personal_assistant/notebook.pkl`

This allows contacts and notes to remain available after restarting the program.

## Example Session

```text
add John 1234567890
add-phone John 0987654321
set-email John john@example.com
set-address John 12 Green Street
set-birthday John 15.08.1995
add-note Buy milk after work
find John
all-notes
exit
```
