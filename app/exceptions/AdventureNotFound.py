from .BaseAppException import BaseAppException

class AdventureNotFound(BaseAppException):
    """Raised when an adventure was looked for but not found"""
    def __init__(self, message: str = "Adventure not found"):
        super().__init__(message, status_code=404)