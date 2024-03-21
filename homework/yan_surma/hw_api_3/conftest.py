import pytest
import requests
import allure


@pytest.fixture()
def new_object_id():
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
    with allure.step('Run post request to create a new object'):
        response = requests.post('https://api.restful-api.dev/objects',
                                 json=body,
                                 headers=headers)
    object_id = response.json()["id"]
    yield object_id
    with allure.step('Delete test object'):
        requests.delete(f'https://api.restful-api.dev/objects/{object_id}')
