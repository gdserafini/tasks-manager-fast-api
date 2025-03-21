from fastapi.testclient import TestClient
import pytest
from tests.app_test import app_test
from src.model.db_schemas import table_registry
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from config.settings import Settings
from src.service.session import get_session
from src.service.security import get_password_hash
from src.utils.factory import UserFactory
from testcontainers.postgres import PostgresContainer


settings = Settings()


@pytest.fixture
def client(session):
    def get_session_override():
        return session
    with TestClient(app_test) as client:
        app_test.dependency_overrides[get_session] = get_session_override
        yield client
    app_test.dependency_overrides.clear()


def _get_user(session):
    password = Settings().PASSWORD_TEST
    user_mock = UserFactory(
        password=get_password_hash(password)
    )
    session.add(user_mock)
    session.commit()
    session.refresh(user_mock)
    user_mock.clean_password = password
    return user_mock


@pytest.fixture
def user(session): return _get_user(session)


@pytest.fixture
def other_user(session): return _get_user(session)


@pytest.fixture
def mock_user():
    return {
        'username': 'test',
        'email': 'test@test.com',
        'password': 'password'
    }


@pytest.fixture
def mock_response():
    return [
        {   
            'id': 1,
            'username': 'test',
            'email': 'test@test.com'
        },
        {
            'id': 2,
            'username': 'test',
            'email': 'test@test.com'
        }
    ]


@pytest.fixture(scope='session')
def engine():
    with PostgresContainer('postgres:16', driver='psycopg') as postgres:
        _engine = create_engine(postgres.get_connection_url())
        with _engine.begin():
            yield _engine


@pytest.fixture(scope='function')
def session(engine):
    table_registry.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
    table_registry.metadata.drop_all(engine)


@pytest.fixture
def token(client, user):
    response = client.post(
        '/auth/token',
        data={
            'username': user.email,
            'password': user.clean_password
        }
    )
    return response.json()['access_token']
