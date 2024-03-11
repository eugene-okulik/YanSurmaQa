import pytest
import requests


@pytest.fixture(scope='session')
def start_session():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture()
def set_up():
    print('before test')
    yield
    print('after test')


@pytest.fixture()
def new_object_id_and_clear():
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {'Content-type': 'application/json'}
    response = requests.post('https://api.restful-api.dev/objects',
                             json=body,
                             headers=headers)
    object_id = response.json()['id']
    print(f'add {object_id}')
    yield object_id
    print(f'delete object {object_id}')
    requests.delete(f'https://api.restful-api.dev/objects/{object_id}')


@pytest.mark.critical
def test_add_object(start_session, set_up):
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {'Content-type': 'application/json'}
    response = requests.post('https://api.restful-api.dev/objects',
                             json=body,
                             headers=headers)
    assert response.status_code == 200, 'Invalid status code'
    print('Add object')
    print(response.json())


@pytest.mark.medium
def test_get_object(set_up, new_object_id_and_clear):
    response = requests.get(f'https://api.restful-api.dev/objects/{new_object_id_and_clear}')
    assert response.status_code == 200
    print('Get object')
    print(response.json())


def test_put_object(set_up, new_object_id_and_clear):
    body = {
        "name": "Apple MacBook M3 Pro",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {'Content-type': 'application/json'}
    response = requests.put(f'https://api.restful-api.dev/objects/{new_object_id_and_clear}',
                            json=body,
                            headers=headers)
    assert response.status_code == 200, 'Invalid status code'
    assert response.json()['name'] == "Apple MacBook M3 Pro"
    print('Put object')
    print(response.json())


def test_patch_object(set_up, new_object_id_and_clear):
    body = {
        "name": "Dell G15 2024 (updated)"
    }
    headers = {'Content-type': 'application/json'}
    response = requests.patch(f'https://api.restful-api.dev/objects/{new_object_id_and_clear}',
                              json=body,
                              headers=headers)
    assert response.status_code == 200, 'Invalid status code'
    assert response.json()['name'] == 'Dell G15 2024 (updated)'
    print('Patch object')
    print(response.json())


def test_delete_object(set_up, new_object_id_and_clear):
    response = requests.delete(f'https://api.restful-api.dev/objects/{new_object_id_and_clear}')
    assert response.status_code == 200, 'Invalid status code'
    print('Delete object')
    print(response.json())
