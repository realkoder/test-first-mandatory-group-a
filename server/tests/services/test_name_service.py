import pytest
import random
from app.services.name_service import get_random_name_gender


async def test_get_random_name_gender_single(monkeypatch):
    fake_persons = [{"name": "Alice", "surname": "Smith", "gender": "female"}]
    monkeypatch.setattr("app.services.name_service.NAMES_DATA", fake_persons)
    monkeypatch.setattr(random, "choice", lambda x: x[0])  # deterministic

    result = await get_random_name_gender()
    assert result == {"first_name": "Alice", "last_name": "Smith", "gender": "female"}


async def test_get_random_name_gender_multiple(monkeypatch):
    fake_persons = [
        {"name": "Alice", "surname": "Smith", "gender": "female"},
        {"name": "Bob", "surname": "Johnson", "gender": "male"}
    ]
    monkeypatch.setattr("app.services.name_service.NAMES_DATA", fake_persons)
    monkeypatch.setattr(random, "choice", lambda x: x[1])  # pick second

    result = await get_random_name_gender()
    assert result == {"first_name": "Bob", "last_name": "Johnson", "gender": "male"}


async def test_get_random_name_gender_empty(monkeypatch):
    monkeypatch.setattr("app.services.name_service.NAMES_DATA", [])
    with pytest.raises(IndexError):
        await get_random_name_gender()
