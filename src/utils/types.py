from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from src.service.security import get_current_user
from src.service.session import get_session


T_Session = Annotated[Session, Depends(get_session)]
T_OAuth2From = Annotated[OAuth2PasswordRequestForm, Depends()]
T_CurrentUser = Annotated[dict, Depends(get_current_user)]
