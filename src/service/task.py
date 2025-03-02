from src.model.task import Task, TaskStateEnum
from sqlalchemy.orm import Session
from src.model.db_schemas import TaskModel


#add typos and implement service func
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