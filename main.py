from cli import main
from storage import save_addressbook, load_addressbook, save_notebook, load_notebook


def run() -> None:
    book, notebook = load_addressbook(), load_notebook()
    try:
        main(book, notebook)
    finally:
        save_addressbook(book)
        save_notebook(notebook)

if __name__ == "__main__":
    run()
