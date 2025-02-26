from fastapi.testclient import TestClient
import pytest
from app import app
from src.model.user import table_registry
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from config.settings import Settings
from src.service.session import get_session
from sqlalchemy.pool import StaticPool
from src.model.user import UserModel


settings = Settings()


@pytest.fixture
def client(session):
    def get_session_override():
        return session
    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override
        yield client
    app.dependency_overrides.clear()


@pytest.fixture
def user(session):
    user_mock = UserModel(
        username='test',
        email='email@test.com',
        password='passwordTest'
    )
    session.add(user_mock)
    session.commit()
    session.refresh(user_mock)
    return user_mock


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


@pytest.fixture
def session():
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool
    )
    table_registry.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
    table_registry.metadata.drop_all(engine)
