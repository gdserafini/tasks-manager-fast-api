from src.service.security import get_password_hash, verify_password


def test_encrypted_password():
    password = "password"
    hashed_password = get_password_hash(password)
    assert verify_password(password, hashed_password)


def test_wrong_encrypted_password():
    password = "password"
    hashed_password = get_password_hash(password)
    assert not verify_password('wrong_password', hashed_password)
