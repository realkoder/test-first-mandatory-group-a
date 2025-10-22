import json
import random
from pathlib import Path
from datetime import datetime
from app.repository.repository import _get_person


# Kirsten Schwalbe's DOB.
# EPOCH = datetime.datetime(1914, 3, 10)

# def generate_dob(EPOCH):

async def get_random_cpr_number():
    person = _get_person()

    # Last digit based on gender + 3x random nums
    if person["gender"] == "female":
        last_digit = random.choices([0,2,4,6,8])
    else:
        last_digit = random.choices([1,3,5,7,9])
    three_digits = random.randrange(0,999)


    return {
        "first_name": person["name"],
        "last_name": person["surname"],
        "gender": person["gender"],
        "last_digit": last_digit,
        "three_digits": three_digits
    }
