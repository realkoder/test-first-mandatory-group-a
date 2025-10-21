import pytest
import asyncio
from tortoise import Tortoise
from app.db import init_db

TEST_DB_URL = "sqlite://:memory:"  # in-memory SQLite

@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="function", autouse=True)
async def initialize_db():
    # Initialize in-memory SQLite DB for testing
    await init_db(db_url=TEST_DB_URL, modules={"models": ["app.models.postal_code"]})
    yield
    # Drop DB after test to reset state
    await Tortoise._drop_databases()
