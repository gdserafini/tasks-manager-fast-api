from http import HTTPStatus


def test_create_task_returns_task_201(client, token):
    data = {
        'title': 'Task 1',
        'description': 'Task 1 description.',
        'state': 'todo'
    }
    response = client.post(
        '/task',
        headers={'Authorization': f'Bearer {token}'},
        json=data
    )
    created_at = response.json()['created_at']
    id = response.json()['id']
    data['created_at'] = created_at
    data['id'] = id
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == data
