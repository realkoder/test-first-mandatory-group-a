import json
import random
from pathlib import Path
from app.repository.repository import get_person

async def get_random_name_gender():
    person = get_person()
    return {
        "first_name": person["name"],
        "last_name": person["surname"],
        "gender": person["gender"]
    }
