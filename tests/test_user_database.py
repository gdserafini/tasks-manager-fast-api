from src.model.user import UserModel, table_registy
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session


def test_create_user_db():
    engine = create_engine('sqlite:///:memory:')
    table_registy.metadata.create_all(engine)
    with Session(engine) as session:
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