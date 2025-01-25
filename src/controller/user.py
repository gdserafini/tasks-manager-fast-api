from http import HTTPStatus
from fastapi import APIRouter
from src.model.user import User, UserResponse
from src.model.message import Message


router = APIRouter()


users = [
        {
            'username': 'test',
            'email': 'test@test.com',
            'password': 'password'
        },
        {
            'username': 'test',
            'email': 'test@test.com',
            'password': 'password'
        } 
    ]


@router.post(
    '/user', 
    response_model=UserResponse,
    status_code=HTTPStatus.CREATED)
def create_user(user: User) -> UserResponse:
    return user


@router.get(
        '/users',
        response_model=list[UserResponse],
        status_code=HTTPStatus.OK)
def get_users() -> list[UserResponse]:
    return [UserResponse(**user) for user in users]


@router.get(
        '/user/{user_id}',
        response_model=UserResponse,
        status_code=HTTPStatus.OK)
def get_user_by_id(user_id: int) -> UserResponse:
    return UserResponse(**users[user_id - 1])


@router.delete(
        '/user/{user_id}',
        response_model=Message,
        status_code=HTTPStatus.OK)
def get_user_by_id(user_id: int) -> None:
    return {
        'message': f'User {user_id} deleted successfully'
    }


@router.put(
        '/user/{user_id}',
        response_model=UserResponse,
        status_code=HTTPStatus.OK)
def update_user(user_id: int, user: User) -> UserResponse:
    return UserResponse(**user.model_dump())
