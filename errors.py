from functools import wraps

def input_error(func):
    """Handle common CLI exceptions without crashing the program."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as error:
            return str(error)
        except KeyError as error:
            if error.args and error.args[0]:
                return str(error.args[0])
            return "Contact not found."
        except IndexError:
            return "Not enough arguments. Please check the command format."

    return wrapper
