class BaseError(Exception):
    """
    Base err.
    """
    
    def __init__(self, message: str) -> None:
        super().__init__(message)


class RequestError(BaseError):
    """
    Raised when a request is with some problem.
    """
    
    def __init__(self, message: str) -> None:
        super().__init__(message)
