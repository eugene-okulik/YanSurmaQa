import pytest
import requests
import allure


@pytest.fixture(scope='session')
def start_session():
    print('Start testing')
    yield
    print('End testing')


@pytest.fixture()
def set_up():
    print('Before test')
    yield
    print('After test')


@allure.title('POST: Создание обьекта')
@allure.feature('Smoke run')
@allure.story('Run with parametrize')
@pytest.mark.parametrize('names', ["Lenovo Legion Y7000P", "MSI Prestige 16 AI Evo", "ASUS ROG Strix G18 2024"])
def test_add_object(start_session, set_up, names):
    with allure.step('Preparing test data'):
        body = {
            "name": names,
            "data": {
                "year": 2019,
                "price": 1849.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB"
            }
        }
        headers = {'Content-type': 'application/json'}
    with allure.step('Run post request to create a new object'):
        response = requests.post('https://api.restful-api.dev/objects',
                                 json=body,
                                 headers=headers)
    with allure.step('Check status code is 200'):
        assert response.status_code == 200, 'Invalid status code'
    print(response.json())


@allure.title('GET: Получение информации обьекта')
@allure.feature('Smoke run')
@pytest.mark.critical
def test_get_object(set_up, new_object_id):
    with allure.step('Run get request to object'):
        response = requests.get(f'https://api.restful-api.dev/objects/{new_object_id}')
    with allure.step('Check status code is 200'):
        assert response.status_code == 200
    print(response.json())


@allure.title('Put: Изменение обьекта')
@allure.feature('Smoke run')
@allure.story('Change object')
@pytest.mark.medium
def test_put_object(set_up, new_object_id):
    with allure.step('Preparing test data'):
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
    with allure.step('Run put request to change a object'):
        response = requests.put(f'https://api.restful-api.dev/objects/{new_object_id}',
                                json=body,
                                headers=headers)
    print(response.json())
    with allure.step('Check status code is 200'):
        assert response.status_code == 200, 'Invalid status code'
    with allure.step('Check that object name is Apple MacBook M3 Pro'):
        assert response.json()['name'] == "Apple MacBook M3 Pro"


@allure.title('Patch: Изменение обьекта')
@allure.feature('Smoke run')
@allure.story('Change object')
def test_patch_object(set_up, new_object_id):
    with allure.step('Preparing test data'):
        body = {
            "name": "Dell G15 2024 (Updated Name)"
        }
        headers = {'Content-type': 'application/json'}
    with allure.step('Run put request to change a object'):
        response = requests.patch(f'https://api.restful-api.dev/objects/{new_object_id}',
                                  json=body,
                                  headers=headers)
    with allure.step('Check status code is 200'):
        assert response.status_code == 200, 'Invalid status code'
    with allure.step('Check that object name is Dell G15 2024 (Updated Name)'):
        assert response.json()['name'] == 'Dell G15 2024 (Updated Name)'
    print(response.json())


@allure.title('DELETE: Удаление обьекта')
@allure.feature('Smoke run')
def test_delete_object(set_up, new_object_id):
    with allure.step('Run delete request'):
        response = requests.delete(f'https://api.restful-api.dev/objects/{new_object_id}')
    with allure.step('Check status code is 200'):
        assert response.status_code == 200, 'Invalid status code'
    print(response.json())
    with allure.step('Send get request to check that object deleted'):
        response = requests.get(f'https://api.restful-api.dev/objects/{new_object_id}')
    with allure.step('Checking that the deleted object does not exist'):
        assert response.json() == {'error': f'Oject with id={new_object_id} was not found.'}
