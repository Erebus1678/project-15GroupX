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
            return "Record wasn't found."
        except AttributeError:
            return "Record wasn't found."
        except IndexError:
            return "Not enough arguments. Please check the command format."
        except Exception as error:
            return f"Unexpected error: {error}"

    return wrapper
