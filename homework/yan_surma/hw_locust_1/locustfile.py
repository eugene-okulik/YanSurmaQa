from locust import task, HttpUser

from data import post_body, put_body, patch_body


class ObjectsUser(HttpUser):
    headers = {'Content-type': 'application/json'}
    object_id = None

    def on_start(self):
        response = self.client.post(
            '/objects',
            json=post_body,
            headers=self.headers
        )
        self.object_id = response.json()["id"]

    @task
    def create_object(self):
        self.client.post(
            '/objects',
            json=post_body,
            headers=self.headers
        )

    @task
    def get_object(self):
        self.client.get(
            f'/objects/{self.object_id}'
        )

    @task
    def put_object(self):
        self.client.put(
            f'/objects/{self.object_id}',
            json=put_body,
            headers=self.headers
        )

    @task
    def patch_object(self):
        self.client.patch(
            f'/objects/{self.object_id}',
            json=patch_body,
            headers=self.headers
        )

    def on_stop(self):
        self.client.delete(f'/objects/{self.object_id}')
