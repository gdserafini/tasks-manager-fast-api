from fastapi import APIRouter
from http import HTTPStatus
from fastapi.responses import JSONResponse
from src.model.message import Message


router = APIRouter()


@router.get(
    '/', 
    status_code=HTTPStatus.OK, 
    response_class=JSONResponse,
    response_model=Message
)
def root() -> Message:
    return Message(message="Hello world!")
