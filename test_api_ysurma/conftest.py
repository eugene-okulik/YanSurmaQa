import allure
import pytest

from endpoints.create_object import CreateObject
from endpoints.put_object import PutObject
from endpoints.get_object import GetObject
from endpoints.patch_object import PatchObject
from endpoints.delete_object import DeleteObject


@pytest.fixture()
def create_post_endpoint():
    return CreateObject()


@pytest.fixture()
def create_put_endpoint():
    return PutObject()


@pytest.fixture()
def create_get_endpoint():
    return GetObject()


@pytest.fixture()
def create_patch_endpoint():
    return PatchObject()


@pytest.fixture()
def create_delete_endpoint():
    return DeleteObject()


@pytest.fixture()
def object_id(create_post_endpoint, create_delete_endpoint):
    body = {
        "name": "Lenovo LOQ15 2023",
        "data": {
            "year": 2023,
            "price": 2000,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    create_post_endpoint.create_object(body)
    object_id = create_post_endpoint.object_id
    yield object_id
    create_delete_endpoint.delete_object(object_id)
