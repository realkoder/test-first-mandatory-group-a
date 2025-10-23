import asyncio
import os
from dotenv import load_dotenv
from tortoise import Tortoise
from tortoise.exceptions import DBConnectionError

load_dotenv()

MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DB = os.getenv("MYSQL_DB")

DEFAULT_DB_URL = f"mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"

async def init_db(db_url: str = None, modules: dict = None):
    if modules is None:
        modules = {"models": ["app.models.postal_code"]}

    # Detect test environment
    is_test = os.getenv("PYTHON_ENV") == "test"
    if is_test:
        print("🧪 Test mode detected — using SQLite in-memory DB.")
        db_url = "sqlite://:memory:"
    elif db_url is None:
        db_url = DEFAULT_DB_URL

    max_retries = 10
    retry_delay = 5

    for attempt in range(max_retries):
        try:
            print(f"🔄 Attempting database connection ({attempt + 1}/{max_retries})...")
            await Tortoise.init(db_url=db_url, modules=modules)
            await Tortoise.generate_schemas()

            # If we're using SQLite in test mode, seed data from addresses.sql
            if db_url.startswith("sqlite"):
                await seed_addresses_sqlite()

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


async def seed_addresses_sqlite():
    sql_path = os.path.join(os.path.dirname(__file__), "assets", "addresses_sqlite.sql")

    if not os.path.exists(sql_path):
        print("⚠️ addresses.sql not found, skipping seeding.")
        return

    print(f"🧩 Seeding SQLite with data from {sql_path}")

    conn = Tortoise.get_connection("default")
    with open(sql_path, encoding="utf-8") as f:
        sql_script = f.read()


    for statement in sql_script.split(";"):
        stmt = statement.strip()
        if stmt:
            try:
                await conn.execute_script(stmt + ";")
            except Exception as e:
                print(f"⚠️ Failed to execute statement: {stmt[:50]}... ({e})")

    print("✅ SQLite seeded successfully.")