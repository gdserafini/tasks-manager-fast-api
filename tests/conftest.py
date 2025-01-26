from fastapi.testclient import TestClient
import pytest
from app import app


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