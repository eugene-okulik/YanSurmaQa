import requests

headers = {'Content-type': 'application/json'}


# Создание объекта
def add_object():
    body = {
        "name": "Apple MacBook M3 Pro",
        "data": {
            "year": 2024,
            "price": 5000,
            "CPU model": "M3 2024",
            "Hard disk size": "2 TB"
        }
    }
    response = requests.post('https://api.restful-api.dev/objects', json=body, headers=headers)
    assert response.status_code == 200, 'Invalid status code'
    print(response.status_code)
    print(response.json())
    return response.json()['id']


# Немного дополнительного тестирования
def new_object():
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post('https://api.restful-api.dev/objects', json=body, headers=headers)
    return response.json()['id']


#  Изменение объекта с помощью метода PUT
def put_object():
    object_id = new_object()
    body = {
        "name": "Apple MacBook M3 Pro",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.put(f'https://api.restful-api.dev/objects/{object_id}', json=body, headers=headers)
    assert response.status_code == 200, 'Invalid status code'
    assert response.json()['name'] == "Apple MacBook M3 Pro"
    print(response.status_code)
    print(response.json())


#  Изменение объекта с помощью метода PATCH
def patch_object():
    object_id = new_object()
    body = {
        "name": "Dell G15 2024 (updated)"
    }
    response = requests.patch(f'https://api.restful-api.dev/objects/{object_id}', json=body, headers=headers)
    assert response.status_code == 200, 'Invalid status code'
    assert response.json()['name'] == "Dell G15 2024 (updated)"
    print(response.status_code)
    print(response.json())


# Удаление объекта
def delete_object():
    object_id = new_object()
    response = requests.delete(f'https://api.restful-api.dev/objects/{object_id}')
    assert response.status_code == 200, 'Invalid status code'
    print(response.status_code)
    print(response.json())


add_object()
put_object()
patch_object()
delete_object()
