from sqlalchemy import select
from src.model.task import Task, TaskStateEnum
from sqlalchemy.orm import Session
from src.model.db_schemas import TaskModel


def create_task_service(
    task: Task, session: Session, current_user_id: int
) -> TaskModel:
    db_task = TaskModel(
        title = task.title,
        description = task.description,
        state = TaskStateEnum.TODO,
        user_id = current_user_id
    )
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task


def get_tasks_service(
    session: Session,
    current_user_id: int,
    title: str | None = None,
    state: str | None = None,
    offset: int | None = None,
    limit: int | None = None
) -> list[TaskModel]:
    query = select(TaskModel).where(
        TaskModel.user_id == current_user_id
    )
    if title:
        query = query.filter(TaskModel.title.contains(title))
    if state:
        query = query.filter(TaskModel.state.contains(state))
    tasks_result = session.scalars(
        query.offset(offset).limit(limit)
    ).all()
    return tasks_result