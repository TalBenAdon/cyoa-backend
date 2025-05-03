from exceptions import BaseAppException
class OpenRouterAPIException(BaseAppException):
    """Raised when an openrouter API returns an error"""
    def __init__(self, message:str):
        super().__init__(message, status_code=500)