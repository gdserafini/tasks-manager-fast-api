from fastapi.testclient import TestClient
from app import app
from http import HTTPStatus


client = TestClient(app)


def test_root_returns_hello_world_mesage_200():
    message = {'Mesage': 'Hello world!'}
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == message
