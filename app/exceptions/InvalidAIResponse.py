from exceptions import BaseAppException
class InvalidAIResponse(BaseAppException):
    """Raised when receiving a bad response from AI service"""
    def __init__(self, message: str):
        super().__init__(message, status_code=502)