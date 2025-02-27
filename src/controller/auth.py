from http import HTTPStatus
from fastapi import APIRouter
from src.utils.responses import responses
from src.model.token import Token
from src.service.login import login_service
from src.utils.types import T_OAuth2From, T_Session


router = APIRouter(prefix='/auth', tags=['auth'])


@router.post(
    '/token',
    status_code=HTTPStatus.OK,
    response_model=Token,
    responses={
        **responses['bad_request'],
        **responses['internal_server_error'],
        **responses['unauthorized'],
        **responses['not_found']
    },
    description='Get a JWT token to authenticate using email and password.'
)
def login(session: T_Session,form_data: T_OAuth2From) -> Token:
    return login_service(session, form_data)
