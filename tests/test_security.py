from src.service.security import (
    get_password_hash, verify_password, create_access_token
)
from jwt import decode
from config.settings import Settings


def test_encrypted_password():
    password = "password"
    hashed_password = get_password_hash(password)
    assert verify_password(password, hashed_password)


def test_wrong_encrypted_password():
    password = "password"
    hashed_password = get_password_hash(password)
    assert not verify_password('wrong_password', hashed_password)


def test_create_access_token():
    data = {'test': 'test'}
    token = create_access_token(data)
    decoded_data = decode(
        token, Settings().SECRET_KEY, algorithms=[Settings().ALGORITHM]
    )
    assert decoded_data['test'] == data['test']
    assert decoded_data['exp']
