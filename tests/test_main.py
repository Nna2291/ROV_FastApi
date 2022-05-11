from urllib.parse import urljoin

import requests


class CustomSession(requests.Session):
    def __init__(self, base_url: str):
        super().__init__()
        self.base_url = base_url

    def request(self, method, url, *args, **kwargs):
        url = urljoin(self.base_url, url)
        return super(CustomSession, self).request(method, url, *args, **kwargs)


client = CustomSession('http://127.0.0.1:8000')


def test_index_page():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_engine():
    data = {'pin_1': 2, 'pin_2': 3, 'speed': 100}
    response = client.post('/engines', json=data)
    assert response.status_code == 200
    assert response.text == f'TURNED ON 2 PIN FOR {data["speed"]}'
