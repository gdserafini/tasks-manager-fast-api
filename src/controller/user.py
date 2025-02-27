from http import HTTPStatus
from fastapi import APIRouter
from src.model.exceptions import InvalidLoginException
from src.model.user import User, UserResponse, UserList
from src.model.message import Message
from src.service.user import (
    create_user_service, delete_user_by_id_service, get_all_users_service, 
    get_user_by_id_service, update_user_service
)
from src.service.session import get_session
from fastapi import Depends
from sqlalchemy.orm import Session
from src.utils.responses import responses
from src.service.security import get_current_user
from src.utils.validations import authorize_user


router = APIRouter()


@router.post(
    '/user', 
    response_model=UserResponse,
    status_code=HTTPStatus.CREATED,
    responses={
        **responses['bad_request'],
        **responses['internal_server_error']
    }
)
def create_user(
    user: User, 
    session: Session = Depends(get_session)
) -> UserResponse:
    result = create_user_service(user, session)
    return result


@router.get(
    '/users',
    response_model=UserList,
    status_code=HTTPStatus.OK,
    responses={
        **responses['bad_request'],
        **responses['internal_server_error'],
        **responses['unauthorized']
    }
)
def get_users(
    offset: int = 0, limit: int = 100, 
    session: Session = Depends(get_session),
    current_user: dict = Depends(get_current_user)
) -> list[UserResponse]:
    users = get_all_users_service(offset, limit, session)
    return {'users': users}


@router.get(
    '/user/{user_id}',
    response_model=UserResponse,
    status_code=HTTPStatus.OK,
    responses={
        **responses['bad_request'],
        **responses['internal_server_error'],
        **responses['unauthorized']
    }   
)
def get_user_by_id(
    user_id: int, session: Session = Depends(get_session),
    current_user: dict = Depends(get_current_user)
) -> UserResponse:
    authorize_user(current_user.id, user_id)
    user = get_user_by_id_service(user_id, session)
    return user


@router.delete(
    '/user/{user_id}',
    response_model=Message,
    status_code=HTTPStatus.OK,
    responses={
        **responses['bad_request'],
        **responses['internal_server_error'],
        **responses['unauthorized']
    }
)
def delete_user_by_id(
    user_id: int, session: Session = Depends(get_session),
    current_user: dict = Depends(get_current_user)
) -> Message:
    authorize_user(current_user.id, user_id)
    result = delete_user_by_id_service(user_id, session)
    return result


@router.put(
    '/user/{user_id}',
    response_model=UserResponse,
    status_code=HTTPStatus.OK,
    responses={
        **responses['bad_request'],
        **responses['internal_server_error'],
        **responses['unauthorized']
    } 
)
def update_user(
    user_id: int, user_data: User, 
    session: Session = Depends(get_session),
    current_user: dict = Depends(get_current_user)
) -> UserResponse:
    authorize_user(current_user.id, user_id)
    result = update_user_service(user_id, user_data, session)
    return result
