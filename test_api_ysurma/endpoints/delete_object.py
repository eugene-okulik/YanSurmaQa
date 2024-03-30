import allure
import requests
from endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):

    @allure.step('Delete object data')
    def delete_object(self, object_id):
        self.response = requests.delete(
            f'https://api.restful-api.dev/objects/{object_id}'
        )
        self.json = self.response.json()
        print(f'Delete object with id {object_id}')
        print(self.json)
        return self.response
