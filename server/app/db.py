import asyncio
import os
from dotenv import load_dotenv
from tortoise import Tortoise
from tortoise.exceptions import DBConnectionError

load_dotenv()

MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_PORT = os.getenv('MYSQL_PORT')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_DB = os.getenv('MYSQL_DB')

DEFAULT_DB_URL = f"mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"

async def init_db(db_url: str = DEFAULT_DB_URL, modules: dict = None):
    if modules is None:
        modules = {"models": ["app.models.postal_code"]}

    max_retries = 10
    retry_delay = 5

    for attempt in range(max_retries):
        try:
            print(f"🔄 Attempting database connection ({attempt + 1}/{max_retries})...")

            await Tortoise.init(db_url=db_url, modules=modules)
            await Tortoise.generate_schemas()
            print("✅ Database connected and ready!")
            return

        except DBConnectionError as e:
            print(f"❌ Database connection failed ({attempt + 1}/{max_retries}): {e}")
            if attempt < max_retries - 1:
                print(f"⏳ Retrying in {retry_delay} seconds...")
                await asyncio.sleep(retry_delay)
            else:
                print("💥 All connection attempts failed")
                raise
        except Exception as e:
            print(f"⚠️ Unexpected error: {e}")
            raise
