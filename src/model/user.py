from pydantic import BaseModel, EmailStr, ConfigDict
from sqlalchemy.orm import registry, Mapped, mapped_column
from sqlalchemy import func
from datetime import datetime
        

table_registry = registry()

        
class User(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime
    model_config = ConfigDict(
        from_attributes=True, ser_json_timedelta='iso8601'
    )


class UserDB(User):
    id: int


class UserList(BaseModel):
    users: list[UserResponse]


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
