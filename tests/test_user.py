from http import HTTPStatus
from src.model.user import UserResponse


def test_create_user_returns_user_201(client, mock_user, mock_response):
    response = client.post('/user', json=mock_user)
    assert response.status_code == HTTPStatus.CREATED
    created_at = response.json()['created_at']
    mock = mock_response[0]
    mock['created_at'] = created_at
    assert response.json() == mock


def test_get_users_returns_users_200(client, user, token):
    user_schema = UserResponse.model_validate(user).model_dump()
    user_schema['created_at'] = user_schema['created_at'].isoformat()
    response = client.get(
        '/user/list',
        headers={'Authorization': f'Bearer {token}'}
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': [user_schema]}


def test_get_user_by_id_returns_users_200(client, user, token):
    user_schema = UserResponse.model_validate(user).model_dump()
    user_schema['created_at'] = user_schema['created_at'].isoformat()
    response = client.get(
        f'/user/{user.id}',
        headers={'Authorization': f'Bearer {token}'}
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == user_schema


def test_delete_user_by_id_returns_200(client, user, token):
    response = client.delete(
        f'/user/{user.id}',
        headers={'Authorization': f'Bearer {token}'}
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'message': f'User id={user.id} deleted successfully'
    }


def test_update_user_returns_user_200(client, user, token):
    user_schema = UserResponse.model_validate(user).model_dump()
    user_schema['created_at'] = user_schema['created_at'].isoformat()
    user_schema['username'] = 'newName'
    update_user = {
        'username': 'newName',
        'email': user_schema['email'],
        'password': user.password
    }
    response = client.put(
        f'/user/{user.id}', 
        json=update_user,
        headers={'Authorization': f'Bearer {token}'}
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == user_schema


def test_forbidden_user_operation_403(
    client, user, other_user, token
) -> None:
    user_schema = UserResponse.model_validate(user).model_dump()
    user_schema['created_at'] = user_schema['created_at'].isoformat()
    response = client.get(
        f'/user/{other_user.id}',
        headers={'Authorization': f'Bearer {token}'}
    )
    assert response.status_code == HTTPStatus.FORBIDDEN


def test_create_user_already_exists(client, user):
    user_to_create = {
        'username': user.username,
        'email': user.email,
        'password': user.password
    }
    response = client.post(
        '/user', json=user_to_create
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST
