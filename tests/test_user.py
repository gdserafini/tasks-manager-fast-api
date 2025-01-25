from fastapi.testclient import TestClient
from app import app
from http import HTTPStatus


client = TestClient(app)


def test_create_user_returns_user_201():
    user = {
        'username': 'test',
        'email': 'test@test.com',
        'password': 'password'
    }
    user_response = {
        'username': 'test',
        'email': 'test@test.com'
    }
    response = client.post('/user', json=user)
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == user_response


def test_get_users_returns_users_200():
    users = [
        {
            'username': 'test',
            'email': 'test@test.com'
        },
        {
            'username': 'test',
            'email': 'test@test.com'
        } 
    ]
    response = client.get('/users')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == users


def test_delete_user_by_id_returns_200():
    response = client.delete('/user/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'message': 'User 1 deleted successfully'
    }


def test_update_user_returns_user_200():
    user = {
        'username': 'test',
        'email': 'test@test.com',
        'password': 'password'
    }
    user_response = {
        'username': 'test',
        'email': 'test@test.com',
    }
    response = client.put('/user/1', json=user)
    assert response.status_code == HTTPStatus.OK
    assert response.json() == user_response
