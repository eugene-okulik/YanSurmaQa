import allure
import requests

from endpoints.endpoint import Endpoint


class CreateObject(Endpoint):

    @allure.step('Create object')
    def create_object(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=body,
            headers=headers
        )
        self.json = self.response.json()
        self.object_id = self.json["id"]
        print(f'Create object with id {self.object_id}')
        print(self.json)
        return self.response
