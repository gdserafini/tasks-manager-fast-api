from fastapi import HTTPException


class UserNotFoundException(HTTPException):
    def __init__(self, 
            status_code: int = 404, 
            datail: str = 'User not found',
            user_id: int = None):
        msg = f'User not found: id = {user_id}'
        super().__init__(status_code=status_code, detail=msg)