from sqlalchemy import select
from src.model.exceptions import InvalidLoginException
from src.model.user import UserModel
from sqlalchemy.orm import Session
from src.service.security import verify_password, create_access_token
from fastapi.security import OAuth2PasswordRequestForm
from src.model.token import Token
from http import HTTPStatus
from jwt.exceptions import ExpiredSignatureError, PyJWTError


def login_service(
    session: Session, 
    form_data: OAuth2PasswordRequestForm
) -> Token:
    user = session.scalar(
        select(UserModel).where(UserModel.email == form_data.username)
    )
    if not user or \
            not verify_password(form_data.password, user.password):
        raise InvalidLoginException(
            detail='Invalid credentials.',
            status_code=HTTPStatus.BAD_REQUEST
        )
    else:
        token_jwt = create_access_token({'sub': user.email})
        return Token(
            token_type='Bearer',
            access_token=token_jwt
        )
    

def refresh_access_token_service(user: UserModel) -> Token:
    try:
        new_access_token = create_access_token(
            data={'sub': user.email}
        )
        return Token(
            token_type='Bearer',
            access_token=new_access_token
        )
    except ExpiredSignatureError:
        raise InvalidLoginException(detail='Expired token.')
    except PyJWTError:
        raise InvalidLoginException(detail='Invalid token.')
