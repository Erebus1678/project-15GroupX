from typing import List, Tuple

from addressbook import AddressBook
from notebook import NoteBook


def parse_input(user_input: str) -> Tuple[str, List[str]]:
    user_input = user_input.strip()
    if not user_input:
        return "", []

    parts = user_input.split()
    command = parts[0].lower()
    args = parts[1:]
    return command, args


def main() -> None:
    address_book = AddressBook()
    notebook = NoteBook()

    print("Personal Assistant project skeleton is ready.")
    print("TASK-0 includes the project structure, README, and module contracts.")
    print("Next steps: TASK-1 AddressBook, TASK-2 NoteBook, TASK-3 Storage, TASK-4 CLI.")

    _ = address_book, notebook


if __name__ == "__main__":
    main()
