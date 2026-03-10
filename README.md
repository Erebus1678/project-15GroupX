# Personal Assistant

`Personal Assistant` is a team CLI application in Python for managing contacts and notes with persistent local storage.

## Project Goal

The project is being developed as a final team assignment for the Python course. The goal is to build a practical command-line assistant that combines contact management, note management, data validation, and persistent storage in one application.

## Planned Functionality

- add, edit, delete, and search contacts
- store contact name, address, phone numbers, email, and birthday
- validate phone numbers, email addresses, and birthday values
- show contacts with upcoming birthdays for a specified number of days
- add, edit, delete, and search notes
- save data locally so it is preserved between application restarts
- provide a clear and convenient CLI workflow

## Optional Extensions

The project may later be expanded with:

- tags for notes
- note search and sorting by tags or keywords
- smart command suggestions for mistyped input

## Planned Architecture

The base project structure is planned around separate modules with clear responsibilities:

- `address_book` - contact domain models and business logic
- `notebook` - notes domain models and operations
- `storage` - loading and saving application data
- `cli` - command parsing, handlers, and user interaction flow
- `tests` - unit and integration checks

This structure will be finalized during `TASK-0`.

## Engineering Principles

- modular design with clear contracts between components
- object-oriented approach with explicit domain entities
- validation at the field level
- resilient error handling for CLI input
- clean, readable code following `PEP 8`

## Team Workflow

The project is intended to be developed through separate task branches and pull requests with code review before merging.


## Setup and Usage

Detailed installation and launch instructions will be added after the initial project skeleton is prepared.


