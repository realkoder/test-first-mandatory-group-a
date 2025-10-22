import json
import random
from pathlib import Path
from app.repository.repository import _get_person


async def get_random_name_gender():
    person = _get_person()
    return {
        "first_name": person["name"],
        "last_name": person["surname"],
        "gender": person["gender"]
    }
