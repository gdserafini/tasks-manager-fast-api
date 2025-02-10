from fastapi.testclient import TestClient
import pytest
from app import app
from src.model.user import table_registy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from config.settings import Settings


settings = Settings()


@pytest.fixture
def client():
    return TestClient(app)


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
            'username': 'test',
            'email': 'test@test.com',
            'id': 2
        }
    ]


@pytest.fixture
def session():
    engine = create_engine(settings.DATABASE_URL)
    table_registy.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
    table_registy.metadata.drop_all(engine)
