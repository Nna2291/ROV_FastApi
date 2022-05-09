from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_index_page():
    response = client.get()
