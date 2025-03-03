from pydantic import BaseModel
from enum import Enum
from pydantic import BaseModel, ConfigDict
from datetime import datetime


class TaskStateEnum(str, Enum):
    DRAFT = 'draft'
    TODO = 'todo'
    DOING = 'doing'
    DONE = 'done'
    TRASE = 'trash'


class Task(BaseModel):
    title: str
    description: str
    state: TaskStateEnum = TaskStateEnum.DRAFT


class TaskResponse(Task):
    id: int
    created_at: datetime
    model_config = ConfigDict(
        from_attributes=True, ser_json_timedelta='iso8601'
    )


class TasksList(BaseModel):
    tasks: list[TaskResponse]
