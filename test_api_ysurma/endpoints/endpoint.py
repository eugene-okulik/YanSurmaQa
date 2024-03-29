import allure


class Endpoint:
    url = 'https://api.restful-api.dev/objects'
    headers = {'Content-type': 'application/json'}
    response = None
    json = None

    @allure.step('Check that name us the same as sent')
    def check_response_name_is_correct(self, name):
        assert self.json["name"] == name, 'Object name is incorrect!'

    @allure.step('Check status code 200')
    def check_status_code_200(self):
        assert self.response.status_code == 200, 'Status code is not 200'

