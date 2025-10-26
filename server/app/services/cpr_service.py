import json
import random
from pathlib import Path
import datetime
from app.repository.repository import get_person


def generate_dob():
    # Kirsten Schwalbe's DOB.
    epoch = datetime.date(1914, 3, 10)
    today = datetime.date.today()

    delta = today - epoch
    delta_in_days = delta.days

    rand_days = random.randint(0, delta_in_days)

    dob_date = epoch + datetime.timedelta(days=rand_days)
    dob_ddmmyy = dob_date.strftime("%d%m%y")

    return dob_date, dob_ddmmyy

async def generate_cpr_name_gender_dob():
    person = get_person()
    
    # DOB and first 6 CPR digits
    dob = generate_dob()

    # Last digit based on gender + 3x random nums
    if person["gender"] == "female":
        last_digit = random.choice([0,2,4,6,8])
    else:
        last_digit = random.choice([1,3,5,7,9])
        
    three_digits = random.randrange(0,999)
    three_digits_str = f"{three_digits:03d}"

    four_digits = f"{three_digits_str}{last_digit}"

    cpr = f"{dob[1]}-{four_digits}"

    return {
        "cpr": cpr,
        "first_name": person["name"],
        "last_name": person["surname"],
        "gender": person["gender"],
        "dob": dob[0],
    }

async def generate_cpr():
    person = get_person()

    # DOB and first 6 CPR digits
    dob = generate_dob()

    # Last digit based on gender + 3x random nums
    if person["gender"] == "female":
        last_digit = random.choice([0,2,4,6,8])
    else:
        last_digit = random.choice([1,3,5,7,9])
        
    three_digits = random.randrange(0,999)
    three_digits_str = f"{three_digits:03d}"

    four_digits = f"{three_digits_str}{last_digit}"

    cpr = f"{dob[1]}-{four_digits}"

    return {
        "cpr": cpr
    }

async def generate_name_gender_dob():
    person = get_person()
    dob = generate_dob()

    return {
        "first_name": person["name"],
        "last_name": person["surname"],
        "gender": person["gender"],
        "dob": dob[0],
    }

async def generate_cpr_name_gender():
    person = get_person()
    dob = generate_dob()

    # Last digit based on gender + 3x random nums
    if person["gender"] == "female":
        last_digit = random.choice([0,2,4,6,8])
    else:
        last_digit = random.choice([1,3,5,7,9])
        
    three_digits = random.randrange(0,999)
    three_digits_str = f"{three_digits:03d}"

    four_digits = f"{three_digits_str}{last_digit}"

    cpr = f"{dob[1]}-{four_digits}"

    return {
        "cpr": cpr,
        "first_name": person["name"],
        "last_name": person["surname"],
        "gender": person["gender"],
    }

