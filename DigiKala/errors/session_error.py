

class SessionInvalid(Exception):
    def __init__(self) -> None:
        message = 'The session is invalid' 
        super().__init__(message)


class SessionExpired(Exception):
    def __init__(self) -> None:
        message = 'The session has expired'
        super().__init__(message)