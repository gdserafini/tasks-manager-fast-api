from pydantic import BaseModel, EmailStr
        
        
class User(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    username: str
    email: EmailStr
