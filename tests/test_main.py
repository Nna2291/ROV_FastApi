import random
from urllib.parse import urljoin

import pytest
import requests


class CustomSession(requests.Session):
    def __init__(self, base_url: str):
        super().__init__()
        self.base_url = base_url

    def request(self, method, url, *args, **kwargs):
        url = urljoin(self.base_url, url)
        return super(CustomSession, self).request(method, url, *args, **kwargs)


client = CustomSession('http://127.0.0.1:8000/')


def test_index_page():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


@pytest.mark.parametrize('execution_number', range(100))
def test_engine(execution_number):
    data = {'pin_1': 2, 'pin_2': 3, 'speed': random.randint(0, 255)}
    response = client.post('/engines', json=data)
    assert response.status_code == 200
    assert response.text == f'"{data["pin_1"]};{data["pin_2"]};{data["speed"]}"'
