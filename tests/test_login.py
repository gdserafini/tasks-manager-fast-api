from http import HTTPStatus
from freezegun import freeze_time


def test_login_with_bearer_token(client, user):
    response = client.post(
        '/auth/token',
        data={
            'username': user.email,
            'password': user.clean_password
        }
    )
    token = response.json()
    assert response.status_code == HTTPStatus.OK
    assert token['token_type'] == 'Bearer'
    assert 'access_token' in token


def test_login_with_wrong_password(client, user):
    wrong_password = 'WrongPassword'
    response = client.post(
        '/auth/token',
        data={
            'username': user.email,
            'password': wrong_password
        }
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_login_with_wrong_email(client, user):
    wrong_email = 'WrongEmail@email.com'
    response = client.post(
        '/auth/token',
        data={
            'username': wrong_email,
            'password': user.clean_password
        }
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_token_expire_after_time(client, user):
    with freeze_time('2025-01-01 00:00:00'):
        response = client.post(
            '/auth/token',
            data = {
                'username': user.email,
                'password': user.clean_password
            }
        )
        assert response.status_code == HTTPStatus.OK
        token = response.json()['access_token']
        with freeze_time('2025-01-01 00:30:01'):
            response = client.get(
                f'/user/{user.id}',
                headers={'Authorization': f'Bearer {token}'}
            )
            assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_refresh_token_logged_user(client, token):
    response = client.post(
        '/auth/token/refresh',
        headers={'Authorization': f'Bearer {token}'}
    )
    data = response.json()
    assert response.status_code == HTTPStatus.OK
    assert 'access_token' in data
    assert 'token_type' in data
    assert data['token_type'] == 'Bearer'


def test_refresh_token_expired_session(client, user):
    with freeze_time('2025-01-01 00:00:00'):
        response = client.post(
            '/auth/token',
            data = {
                'username': user.email,
                'password': user.clean_password
            }
        )
        assert response.status_code == HTTPStatus.OK
        token = response.json()['access_token']
        with freeze_time('2025-01-01 00:30:01'):
            response = client.post(
                '/auth/token/refresh',
                headers={'Authorization': f'Bearer {token}'}
            )
            assert response.status_code == HTTPStatus.UNAUTHORIZED
