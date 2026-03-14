from functools import wraps


class AssistantError(Exception):
    """Base application error shown to CLI users."""


class ValidationError(AssistantError):
    """Raised when user input fails validation."""


class ContactNotFoundError(AssistantError):
    """Raised when a contact cannot be found."""


class NoteNotFoundError(AssistantError):
    """Raised when a note cannot be found."""


class DuplicateContactError(AssistantError):
    """Raised when creating a contact that already exists."""


class DuplicateNoteError(AssistantError):
    """Raised when creating a note with an existing id."""


class DuplicatePhoneError(AssistantError):
    """Raised when adding a phone that already exists."""


class PhoneNotFoundError(AssistantError):
    """Raised when a phone cannot be found in a record."""


def input_error(func):
    """Handle common CLI exceptions without crashing the program."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except AssistantError as error:
            return str(error)

    return wrapper
