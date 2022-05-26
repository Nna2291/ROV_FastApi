import random
from urllib.parse import urljoin

import pytest
import requests

from models.telemetry import Telemetry


class CustomSession(requests.Session):
    def __init__(self, base_url: str):
        super().__init__()
        self.base_url = base_url

    def request(self, method, url, *args, **kwargs):
        url = urljoin(self.base_url, url)
        return super(CustomSession, self).request(method, url, *args, **kwargs)


client = CustomSession('http://raspberrypi.local:8000/')


def test_index_page():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


@pytest.mark.parametrize('execution_number', range(49))
def test_engine(execution_number):
    data = {'task': 'POST', 'pin_1': random.choice([2, 3]), 'pin_2': 3,
            'speed': random.randint(0, 255)}
    response = client.post('/engines', json=data)
    assert response.status_code == 200
    assert response.text == '"ok"'


@pytest.mark.parametrize('execution_number', range(49))
def test_data(execution_number):
    data = {'task': 'GET'}
    response = client.get('/data', json=data)
    assert response.status_code == 200
    Telemetry(**response.json())


def test_engine_off():
    data = {'task': 'POST', 'pin_1': 2, 'pin_2': 3,
            'speed': 0}
    response = client.post('/engines', json=data)
    assert response.status_code == 200
    assert response.text == '"ok"'
    data = {'task': 'POST', 'pin_1': 3, 'pin_2': 3,
            'speed': 0}
    response = client.post('/engines', json=data)
    assert response.status_code == 200
    assert response.text == '"ok"'
