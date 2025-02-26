from zoneinfo import ZoneInfo
from pwdlib import PasswordHash
from datetime import datetime, timedelta
from jwt import encode
from config.settings import Settings


pwd_context = PasswordHash.recommended()


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(
    plain_password: str, hashed_password: str
) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(
        ZoneInfo('UTC')) + \
        timedelta(minutes=Settings().ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({'exp': expire})
    token_jwt = encode(
        to_encode, 
        Settings().SECRET_KEY, algorithm=Settings().ALGORITHM
    )
    return token_jwt