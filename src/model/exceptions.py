from fastapi import HTTPException
from http import HTTPStatus


class UserNotFoundException(HTTPException):
    def __init__(self, 
            status_code: int = HTTPStatus.NOT_FOUND, 
            datail: str = 'User not found',
            user_id: int = None):
        msg = f'User not found: id = {user_id}'
        super().__init__(status_code=status_code, detail=msg)


class UserAlreadyExistsException(HTTPException):
    def __init__(self, 
            status_code: int = HTTPStatus.BAD_REQUEST, 
            detail: str = 'User already exists',
            username: str = None,
            email: str = None):
        msg = f'User already exists: username = {username}, email = {email}'
        super().__init__(status_code=status_code, detail=msg)