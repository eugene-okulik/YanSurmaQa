from endpoints.endpoint import Endpoint
import requests
import allure


class PutObject(Endpoint):

    @allure.step('Put object data')
    def put_changes_to_object(self, body, object_id, headers=None):
        headers = headers if headers else self.headers
        put_url = f'{self.url}/{object_id}'
        self.response = requests.put(
            put_url,
            json=body,
            headers=headers
        )
        self.json = self.response.json()
        print(f'Put object with id {self.json["id"]}')
        print(self.json)
        return self.response
