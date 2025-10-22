import json
import random
from pathlib import Path
import datetime
from app.repository.repository import get_person


# Kirsten Schwalbe's DOB.
epoch = datetime.datetime(1914, 3, 10,0,00,00,00)

def generate_dob(epoch):
    today = datetime.datetime.now()

    delta = today - epoch
    delta_in_days = delta.days
    rand_days = random.randrange(0, delta_in_days)


    return today, epoch, delta, delta_in_days, rand_days

async def get_random_cpr_number():
    person = get_person()

    # Last digit based on gender + 3x random nums
    if person["gender"] == "female":
        last_digit = random.choices([0,2,4,6,8])
    else:
        last_digit = random.choices([1,3,5,7,9])
    three_digits = random.randrange(0,999)
    three_digits_str = f"{three_digits:03d}"

    four_digits = f"{three_digits:03d}{last_digit}"

    dob = generate_dob(epoch)

    return {
        "first_name": person["name"],
        "last_name": person["surname"],
        "gender": person["gender"],
        "last_digit": last_digit,
        "three_digits": three_digits,
        "three_digits_str": three_digits_str,
        "four_digits": four_digits,
        "today": dob[0],
        "epoch": dob[1],
        "delta": dob[2],
        "delta_in_days": dob[3],
        "rand_days": dob[4],
    }
