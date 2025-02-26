from sqlalchemy import select
from src.model.exceptions import UserAlreadyExistsException, UserNotFoundException
from src.model.message import Message
from src.model.user import User
from src.model.user import UserModel
from sqlalchemy.orm import Session
from src.service.security import get_password_hash


def create_user_service(user: User, session: Session) -> UserModel:
    result = session.scalar(
        select(UserModel).where(
            (UserModel.username == user.username) |
            (UserModel.email == user.email)
        )
    )
    if result:
        if result.username == user.username:
            raise UserAlreadyExistsException(username=user.username)
        elif result.email == user.email:
            raise UserAlreadyExistsException(email=user.email)
    user_db = UserModel(
        username=user.username,
        email=user.email,
        password=get_password_hash(user.password)
    )
    session.add(user_db)
    session.commit()
    session.refresh(user_db)
    return user_db


def get_all_users_service(
    offset: int, limit: int, session: Session
) -> list[UserModel]:
    if offset < 0 or limit < 0 or \
            type(offset) != int or type(limit) != int:
        raise ValueError('Invalid params.')
    users = session.scalars(
        select(UserModel).offset(offset).limit(limit)
    ).all()
    return users


def get_user_by_id_service(
        user_id: int, session: Session
) -> UserModel:
    user = session.scalar(
        select(UserModel).where(UserModel.id == user_id)
    )
    if not user:
        raise UserNotFoundException(user_id=user_id)
    return user


def delete_user_by_id_service(
    user_id: int, session: Session
) -> Message:
    user = get_user_by_id_service(user_id, session)
    session.delete(user)
    session.commit()
    return Message(
        message=f'User id={user_id} deleted successfully'
    )
    

def update_user_service(
    user_id: int, user: User, session: Session
) -> UserModel:
    user_db = get_user_by_id_service(user_id, session)
    user_db.username = user.username
    user_db.email = user.email
    user_db.password = get_password_hash(user.password)
    session.commit()
    session.refresh(user_db)
    return user_db