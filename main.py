from addressbook import AddressBook
from notebook import NoteBook
from storage import load_data, save_data
from cli import main

def run():
    try:
        book, notebook = load_data()
    except NotImplementedError:
        book, notebook = AddressBook(), NoteBook()

    try:
        main(book, notebook)
    finally:
        try:
            save_data(book, notebook)
        except NotImplementedError:
            pass

if __name__ == "__main__":
    run()
