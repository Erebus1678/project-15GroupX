from cli import main
from storage import save_addressbook, load_addressbook, save_notebook, load_notebook


def run() -> None:
    book, notebook = load_addressbook(), load_notebook()

    def save_state() -> None:
        save_addressbook(book)
        save_notebook(notebook)

    try:
        main(book, notebook, save_state)
    finally:
        save_state()

if __name__ == "__main__":
    run()
