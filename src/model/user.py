from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime

        
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
