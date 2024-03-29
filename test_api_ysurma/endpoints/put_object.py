from test_api_ysurma.endpoints.endpoint import Endpoint
import requests
import allure


class PutObject(Endpoint):

    @allure.step('Update object data')
    def put_changes_to_object(self, object_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{object_id}',
            json=body,
            headers=headers
        )
        self.json = self.response.json()
