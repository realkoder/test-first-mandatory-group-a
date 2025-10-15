import json
import random
from pathlib import Path

with open("app/assets/person-names.json", "r", encoding="utf-16") as f:
    data = json.load(f)
    NAMES_DATA = data["persons"]

async def get_random_name_gender():
    person = random.choice(NAMES_DATA)
    return {
        "first_name": person["name"],
        "last_name": person["surname"],
        "gender": person["gender"]
    }
