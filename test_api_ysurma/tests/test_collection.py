import pytest
from data import TEST_DATA, NEGATIVE_TEST_DATA


@pytest.mark.parametrize('data', TEST_DATA)
def test_create_object(create_post_endpoint, data):
    create_post_endpoint.create_object(body=data)
    create_post_endpoint.check_status_code_200()
    create_post_endpoint.check_response_name_is_correct(data["name"])


@pytest.mark.parametrize('data', NEGATIVE_TEST_DATA)
def test_create_object_with_invalid_names(create_post_endpoint, data):
    create_post_endpoint.create_object(body=data)
    create_post_endpoint.check_status_code_200()
    create_post_endpoint.check_response_name_is_correct(data["name"])


def test_put_object(create_put_endpoint, object_id):
    body = {
        "name": "Apple MacBook M3 Pro",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    create_put_endpoint.put_changes_to_object(body, object_id)
    create_put_endpoint.check_status_code_200()
    create_put_endpoint.check_response_name_is_correct(body["name"])


def test_get_object(create_get_endpoint, object_id):
    create_get_endpoint.get_object_data(object_id)
    create_get_endpoint.check_status_code_200()


def test_patch_object(create_patch_endpoint, object_id):
    body = {
        "name": "Asus GOR Strix 2024 (Updated Name)"
    }
    create_patch_endpoint.patch_changes_to_object(body, object_id)
    create_patch_endpoint.check_status_code_200()
    create_patch_endpoint.check_response_name_is_correct(body["name"])


def test_delete_object(create_delete_endpoint, object_id, create_get_endpoint):
    create_delete_endpoint.delete_object(object_id)
    create_delete_endpoint.check_status_code_200()
    create_get_endpoint.get_object_data(object_id)
    create_get_endpoint.check_that_object_doesnt_exists(object_id)
