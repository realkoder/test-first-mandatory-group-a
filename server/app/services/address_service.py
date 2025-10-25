from typing import Any, Dict
from faker import Faker
import random
from app.models.postal_code import PostalCode

fake = Faker('da_DK')


async def get_random_address() -> Dict[str, Any]:
    street = _get_street_name()
    number = _get_random_street_number()
    floor = _get_random_floor()
    door = _get_random_door()
    postal_code_obj = await _get_random_postal_code()

    address_data = {
        "street": street,
        "number": number,
        "floor": floor,
        "door": door,
        "postal_code": postal_code_obj.postal_code,
        "town_name": postal_code_obj.town_name,
        "full_address": f"{street} {number}, {floor}. {door}, {postal_code_obj.postal_code} {postal_code_obj.town_name}"
    }

    return address_data


def _get_street_name():
    return fake.street_name()


def _get_random_street_number():
    """Return a number from 1–999, optionally followed by an uppercase letter."""
    number = random.randint(1, 999)
    if random.random() < 0.3:  # ~30% chance of having a letter suffix
        letter = chr(random.randint(ord('A'), ord('Z')))
        return f"{number}{letter}"
    return str(number)


def _get_random_floor():
    """Return either 'st' or a number from 1–99."""
    return 'st' if random.random() < 0.2 else str(random.randint(1, 99))


def _get_random_door():
    choice = random.choice(['th', 'mf', 'tv', 'number', 'complex'])
    if choice == 'number':
        return str(random.randint(1, 50))
    elif choice == 'complex':
        letter = chr(random.randint(ord('a'), ord('z')))
        if random.random() < 0.5:
            digits = random.randint(1, 999)
            return f"{letter}{digits}"
        else:
            digits = random.randint(1, 999)
            return f"{letter}-{digits}"
    else:
        return choice


async def _get_random_postal_code() -> PostalCode:
    count = await PostalCode.all().count()
    if count == 0:
        raise ValueError("No postal codes available in database")

    # Get random offset
    random_offset = random.randint(0, count - 1)

    # Get the postal code at random offset
    postal_code = await PostalCode.all().offset(random_offset).first()
    return postal_code
