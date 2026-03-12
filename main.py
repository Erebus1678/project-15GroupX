from addressbook import AddressBook
from notebook import NoteBook
from cli import main

def run():
    book, notebook = AddressBook(), NoteBook()
    main(book, notebook)

if __name__ == "__main__":
    run()
