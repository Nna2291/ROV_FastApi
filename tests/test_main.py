from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_index_page():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_engine():
    data = {'pin_1': 2, 'pin_2': 3, 'speed': 100}
    response = client.post('/engines', json=data)
    assert response.status_code == 200
    assert response.json() == {'Successfully turn on engine': {
        'pin_1': data['pin_1'],
        'pin_2': data['pin_2'],
        'speed': data['speed']
    }}
