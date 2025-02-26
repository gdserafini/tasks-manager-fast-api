from sqlalchemy import select
from src.model.exceptions import InvalidLoginException
from src.model.user import UserModel
from sqlalchemy.orm import Session
from src.service.security import verify_password, create_access_token
from fastapi.security import OAuth2PasswordRequestForm
from src.model.token import Token


def login_service(
    session: Session, 
    form_data: OAuth2PasswordRequestForm
) -> Token:
    user = session.scalar(
        select(UserModel).where(UserModel.email == form_data.username)
    )
    if not user or not verify_password(
        form_data.password, user.password
    ):
        raise InvalidLoginException()
    else:
        token_jwt = create_access_token({'sub': user.email})
        return Token(
            token_type='Bearer',
            access_token=token_jwt
        )