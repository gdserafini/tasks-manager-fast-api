from src.model.db_schemas import UserModel
from sqlalchemy import select


def test_create_user_db(session):
    user = UserModel(
        username="Username",
        email="username@email.com",
        password='password'
    )
    session.add(user)
    session.commit()
    result = session.scalar(
        select(UserModel).where(UserModel.id == 1)
    )
    assert result.id == 1