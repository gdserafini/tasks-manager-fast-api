from datetime import datetime
from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, registry
from src.model.task import TaskStateEnum


table_registry = registry()


@table_registry.mapped_as_dataclass
class UserModel:
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True, init=False
    )
    username: Mapped[str] = mapped_column(
        unique=True, nullable=False
    )
    password: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    created_at: Mapped[datetime] = mapped_column(
        nullable=False, server_default=func.now(), init=False
    )


@table_registry.mapped_as_dataclass
class TaskModel:
    __tablename__ = 'tasks'
    id: Mapped[int] = mapped_column(
        init=False, primary_key=True, autoincrement=True
    )
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str]
    state: Mapped[TaskStateEnum] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        nullable=False, server_default=func.now(), init=False
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id')
    )
