from app.main import app

import pytest
from fastapi.testclient import TestClient

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "TEST TEST TEST"}

def test_name_gender_success(monkeypatch):
    """Unit test: endpoint logic."""
    async def mock_get_random_name_gender():
        return {"first_name": "John", "last_name": "Doe", "gender": "male"}

    monkeypatch.setattr("app.main.get_random_name_gender", mock_get_random_name_gender)

    response = client.get("/name-gender")
    assert response.status_code == 200
    assert response.json() == {"first_name": "John", "last_name": "Doe", "gender": "male"}


def test_name_gender_integration():
    """Integration test: real endpoint + real data."""
    response = client.get("/name-gender")
    assert response.status_code == 200
    data = response.json()
    assert set(data.keys()) == {"first_name", "last_name", "gender"}
