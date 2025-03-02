from fastapi import APIRouter
from src.model.task import TaskResponse, Task
from src.utils.types import T_Session, T_CurrentUser
from http import HTTPStatus
from src.utils.responses import responses
from src.service.task import create_task_service


router = APIRouter(prefix='/task', tags=['Tasks'])


@router.post(
    '',
    response_model=TaskResponse,
    status_code=HTTPStatus.CREATED,
    responses={
        **responses['bad_request'],
        **responses['internal_server_error'],
        **responses['unauthorized'],
        **responses['forbidden'],
        **responses['unprocessable_entity']
    },
    description='Create a new task as TODO for a logged user.'
)
def create_task(
    task: Task, 
    session: T_Session, 
    current_user: T_CurrentUser
) -> TaskResponse:
    created_task = create_task_service(
        task, session, current_user.id
    )
    return created_task
