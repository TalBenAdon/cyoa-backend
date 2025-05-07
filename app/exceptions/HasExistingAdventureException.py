from .BaseAppException import BaseAppException

class HasExistingAdventureException(BaseAppException):
    """Raised when user has an existing adventure yet start request was sent"""
    def __init__(self, message: str = "User already has an adventure"):
        super().__init__(message, status_code=400)