from http import HTTPStatus
from src.utils.factory import TaskFactory


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


def test_get_tasks_list_returns_tasks_200(
    session, client, user, token
) -> None:
    tasks = TaskFactory.create_batch(
        size=3, user_id=user.id,
        title='title', description='description'
    )
    session.bulk_save_objects(tasks)
    session.commit()
    response = client.get(
        '/task/list?title=title&description=description&offset=0&limit=3',
        headers={'Authorization': f'Bearer {token}'},
    )
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()['tasks']) == len(tasks)
