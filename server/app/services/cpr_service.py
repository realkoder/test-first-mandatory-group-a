import json
import random
from pathlib import Path
import datetime
from app.repository.repository import get_person


# Kirsten Schwalbe's DOB.
epoch = datetime.date(1914, 3, 10)

def generate_dob(epoch):
    today = datetime.date.today()

    delta = today - epoch
    delta_in_days = delta.days

    rand_days = random.randint(0, delta_in_days)

    dob_date = epoch + datetime.timedelta(days=rand_days)
    dob_ddmmyy = dob_date.strftime("%d%m%y")

    return dob_date, dob_ddmmyy

async def get_random_cpr_number():
    person = get_person()
    
    # DOB and first 6 CPR digits
    dob = generate_dob(epoch)

    # Last digit based on gender + 3x random nums
    if person["gender"] == "female":
        last_digit = random.choice([0,2,4,6,8])
    else:
        last_digit = random.choice([1,3,5,7,9])
        
    three_digits = random.randrange(0,999)
    three_digits_str = f"{three_digits:03d}"

    four_digits = f"{three_digits_str}{last_digit}"


    return {
        "first_name": person["name"],
        "last_name": person["surname"],
        "gender": person["gender"],
        "last_digit": last_digit,
        "three_digits": three_digits,
        "three_digits_str": three_digits_str,
        "four_digits": four_digits,
        "dob": dob[0],
        "dob_ddmmyy": dob[1],
    }
