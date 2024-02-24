import locust
import requests


class TestUser(locust.HttpUser):
    wait_time = locust.between(1, 2)

    @locust.task
    def test_api(self):
        res = self.client.get("http://127.0.0.1:5000/test")
        assert res.status_code == 200
