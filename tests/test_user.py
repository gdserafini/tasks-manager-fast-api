from http import HTTPStatus


def test_create_user_returns_user_201(client, mock_user, mock_response):
    response = client.post('/user', json=mock_user)
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == mock_response[0]


def test_get_users_returns_users_200(client, mock_user, mock_response):
    client.post('/user', json=mock_user)
    response = client.get('/users')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == mock_response


def test_get_user_by_id_returns_users_200(client, mock_response):
    response = client.get('/user/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == mock_response[0]


def test_delete_user_by_id_returns_200(client):
    response = client.delete('/user/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'message': 'User 1 deleted successfully'
    }


def test_update_user_returns_user_200(client):
    updated_user = {
        'username': 'test updated',
        'email': 'test@test.com',
        'password': 'password'
    }
    updated_user_response = {
        'id': 1,
        'username': 'test updated',
        'email': 'test@test.com',
    }
    response = client.put('/user/1', json=updated_user)
    print(response.json())
    assert response.status_code == HTTPStatus.OK
    assert response.json() == updated_user_response
