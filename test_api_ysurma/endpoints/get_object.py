import allure
import requests
from endpoints.endpoint import Endpoint


class GetObject(Endpoint):

    @allure.step('Get object data')
    def get_object_data(self, object_id):
        self.response = requests.get(f'{self.url}/{object_id}')
        self.json = self.response.json()
        print(f'Get object info with id {object_id}')
        print(self.json)
        return self.response

    def check_that_object_doesnt_exists(self, object_id):
        error = {'error': f'Oject with id={object_id} was not found.'}
        assert self.json == error
