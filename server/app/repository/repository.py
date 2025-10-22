import random
import json
from pathlib import Path

def get_person():
    with open("app/assets/person-names.json", "r", encoding="utf-16") as f:
        data = json.load(f)
        NAMES_DATA = data["persons"]

    person = random.choice(NAMES_DATA)
    return person


# TODO: Get random address too
