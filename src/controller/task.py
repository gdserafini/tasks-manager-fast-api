from fastapi import APIRouter
from src.model.task import TaskResponse, Task, TasksList, TaskUpdate
from src.utils.types import T_Session, T_CurrentUser
from http import HTTPStatus
from src.utils.responses import responses
from src.service.task import (
    create_task_service, get_tasks_service, delete_task_service,
    patch_task_service
)
from src.model.message import Message


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


@router.get(
    '/list',
    status_code=HTTPStatus.OK,
    response_model=TasksList,
    responses={
        **responses['bad_request'],
        **responses['internal_server_error'],
        **responses['unauthorized'],
        **responses['forbidden']
    },
    description='Get all tasks for a logged user.'
)
def get_tasks(
    session: T_Session,
    current_user: T_CurrentUser,
    title: str | None = None,
    state: str | None = None,
    offset: int | None = None,
    limit: int | None = None
):
    result_tasks = get_tasks_service(
        session=session, current_user_id=current_user.id,
        title=title, state=state, offset=offset, limit=limit
    )
    return {'tasks': result_tasks}


@router.delete(
    '/{task_id}',
    response_model=Message,
    responses={
        **responses['bad_request'],
        **responses['internal_server_error'],
        **responses['unauthorized'],
        **responses['forbidden'],
        **responses['not_found']
    },
    description='Delete a spefic task for a logged user.'
)
def delete_task(
    task_id: int, session: T_Session, 
    current_user: T_CurrentUser
):
    delete_task_service(
        task_id=task_id, session=session,
        current_user_id=current_user.id
    )
    return {'message': 'Task has been deleted successfully.'}


@router.patch(
    '/{task_id}',
    response_model=TaskResponse,
    responses={
        **responses['bad_request'],
        **responses['internal_server_error'],
        **responses['unauthorized'],
        **responses['forbidden'],
        **responses['not_found']
    },
    description='Delete a spefic task for a logged user.'
)
def patch_task(
    task_id: int, session: T_Session,
    current_user: T_CurrentUser, task: TaskUpdate
):
    patched_task = patch_task_service(
        task_id=task_id, session=session,
        current_user_id = current_user.id,
        task=task
    )
    return patched_task
