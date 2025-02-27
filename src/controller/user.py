from http import HTTPStatus
from fastapi import APIRouter
from src.model.user import User, UserResponse, UserList
from src.model.message import Message
from src.service.user import (
    create_user_service, delete_user_by_id_service, get_all_users_service, 
    get_user_by_id_service, update_user_service
)
from src.utils.responses import responses
from src.utils.validations import authorize_user
from src.utils.types import T_Session, T_CurrentUser


router = APIRouter(prefix='/user', tags=['users'])


@router.post(
    '', 
    response_model=UserResponse,
    status_code=HTTPStatus.CREATED,
    responses={
        **responses['bad_request'],
        **responses['internal_server_error']
    }
)
def create_user(user: User, session: T_Session) -> UserResponse:
    return create_user_service(user, session)


@router.get(
    '/list',
    response_model=UserList,
    status_code=HTTPStatus.OK,
    responses={
        **responses['bad_request'],
        **responses['internal_server_error'],
        **responses['unauthorized'],
        **responses['forbidden']
    }
)
def get_users(
    session: T_Session, current_user: T_CurrentUser,
    offset: int = 0, limit: int = 100
) -> list[UserResponse]:
    users = get_all_users_service(offset, limit, session)
    return {'users': users}


@router.get(
    '/{user_id}',
    response_model=UserResponse,
    status_code=HTTPStatus.OK,
    responses={
        **responses['bad_request'],
        **responses['internal_server_error'],
        **responses['unauthorized'],
        **responses['forbidden']
    }   
)
def get_user_by_id(
    user_id: int, session: T_Session, current_user: T_CurrentUser
) -> UserResponse:
    authorize_user(current_user.id, user_id)
    return get_user_by_id_service(user_id, session)


@router.delete(
    '/{user_id}',
    response_model=Message,
    status_code=HTTPStatus.OK,
    responses={
        **responses['bad_request'],
        **responses['internal_server_error'],
        **responses['unauthorized'],
        **responses['forbidden']
    }
)
def delete_user_by_id(
    user_id: int, session: T_Session, current_user: T_CurrentUser
) -> Message:
    authorize_user(current_user.id, user_id)
    return delete_user_by_id_service(user_id, session)


@router.put(
    '/{user_id}',
    response_model=UserResponse,
    status_code=HTTPStatus.OK,
    responses={
        **responses['bad_request'],
        **responses['internal_server_error'],
        **responses['unauthorized'],
        **responses['forbidden']
    } 
)
def update_user(
    user_id: int, user_data: User, 
    session: T_Session, current_user: T_CurrentUser
) -> UserResponse:
    authorize_user(current_user.id, user_id)
    return update_user_service(user_id, user_data, session)
