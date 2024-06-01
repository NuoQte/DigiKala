

class SessionPasswordNeeded(Exception):
    def __init__(self) -> None:
        message = 'a session password is required' 
        super().__init__(message)


class SessionWrongCode(Exception):
    def __init__(self) -> None:
        message = 'The code is wrong' 
        super().__init__(message)

class SessionWrongPassword(Exception):
    def __init__(self) -> None:
        message = 'The Password is wrong' 
        super().__init__(message)



class UsernameInvalid(Exception):
    def __init__(self) -> None:
        message = 'The phone number or email is invalid' 
        super().__init__(message)

