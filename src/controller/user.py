from http import HTTPStatus
from fastapi import APIRouter
from src.model.user import User, UserResponse, UserDB
from src.model.message import Message
from src.model.exceptions import UserNotFoundException


router = APIRouter()
users_db: list[User] = []


def _get_id() -> int:
    return len(users_db) + 1


def validate_user(user_id: int) -> None:
    if user_id < 1 or user_id > len(users_db):
        raise UserNotFoundException(user_id=user_id)


@router.post(
    '/user', 
    response_model=UserResponse,
    status_code=HTTPStatus.CREATED)
def create_user(user: User) -> UserResponse:
    user_db = UserDB(id=_get_id(), **user.model_dump())
    users_db.append(user_db)
    return UserResponse(**user_db.model_dump())


@router.get(
        '/users',
        response_model=list[UserResponse],
        status_code=HTTPStatus.OK)
def get_users() -> list[UserResponse]:
    return [UserResponse(**user.model_dump()) for user in users_db]


@router.get(
        '/user/{user_id}',
        response_model=UserResponse,
        status_code=HTTPStatus.OK)
def get_user_by_id(user_id: int) -> UserResponse:
    validate_user(user_id)
    user = filter(lambda user: user.id == user_id, users_db).__next__()
    return UserResponse(**user.model_dump())


@router.delete(
        '/user/{user_id}',
        response_model=Message,
        status_code=HTTPStatus.OK)
def get_user_by_id(user_id: int) -> None:
    validate_user(user_id)
    users_db.remove(filter(
        lambda user: user.id == user_id, users_db
    ).__next__())
    return {
        'message': f'User {user_id} deleted successfully'
    }


@router.put(
        '/user/{user_id}',
        response_model=UserResponse,
        status_code=HTTPStatus.OK)
def update_user(user_id: int, user: User) -> UserResponse:
    global users_db
    validate_user(user_id)
    users_db = [
        existing_user 
        for existing_user in users_db if existing_user.id != user_id
    ]
    updated_user = UserDB(id=user_id, **user.model_dump())
    users_db.append(updated_user)
    return UserResponse(**updated_user.model_dump())
