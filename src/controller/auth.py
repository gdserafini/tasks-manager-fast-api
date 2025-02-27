from http import HTTPStatus
from fastapi import APIRouter
from fastapi import Depends
from src.utils.responses import responses
from fastapi.security import OAuth2PasswordRequestForm
from src.service.session import get_session
from sqlalchemy.orm import Session
from src.model.token import Token
from src.service.login import login_service


router = APIRouter()


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
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session)
) -> Token:
    token_response = login_service(session, form_data)
    return token_response
