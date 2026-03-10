# Personal Assistant

`Personal Assistant` is a team CLI application in Python for managing contacts and notes.

## Current Stage

The repository currently contains only `TASK-0` - `Project Init & Contracts`.

At this stage the project includes:

- project skeleton
- README
- module split by responsibility
- stub classes and method signatures for the next tasks

## Project Structure

```text
main.py
addressbook.py
notebook.py
storage.py
errors.py
README.md
```

## Module Roles

- `main.py` - entry point and minimal application scaffold
- `addressbook.py` - contracts for contact fields, records, and address book operations
- `notebook.py` - contracts for notes and notebook operations
- `storage.py` - contracts for saving and loading data
- `errors.py` - shared error-handling decorator for future CLI commands

## Roadmap

1. `TASK-0` - project skeleton, stubs, README
2. `TASK-1` - AddressBook module with validation, CRUD, search, birthdays
3. `TASK-2` - NoteBook module with add/edit/delete/search
4. `TASK-3` - unified pickle-based storage
5. `TASK-4` - CLI dispatcher and command loop
6. `TASK-5` - integration of all modules

## Run

Current scaffold can be started with:

```bash
python main.py
```

At the moment it only confirms that the project skeleton is ready. Full functionality will be added in the next tasks.
