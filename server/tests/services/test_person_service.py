import datetime
import pytest
from app.services.person_service import generate_person


# ===========================================================================================
# PERSON SERVICE INTEGRATION TEST
# ==========================================================================================
@pytest.mark.parametrize("key, validator", [
    # ======================================
    # CPR VALIDATION
    # ======================================
    ("cpr", lambda person: isinstance(person["cpr"], str) and len(person["cpr"]) == 11),

    # ======================================
    # FIRST_NAME VALIDATION
    # ======================================
    ("first_name", lambda person: isinstance(person["first_name"], str) and 1 <= len(person["first_name"]) <= 30),

    # ======================================
    # LAST_NAME VALIDATION
    # ======================================
    ("last_name", lambda person: isinstance(person["last_name"], str) and 1 <= len(person["last_name"]) <= 30),

    # ======================================
    # GENDER VALIDATION
    # ======================================
    ("gender", lambda person: person["gender"] in ['female', 'male']),

    # ======================================
    # DOB VALIDATION
    # ======================================
    ("dob", lambda person: isinstance(person["dob"], datetime.date) and
                           person["dob"].year >= 1914 and
                           person["dob"] <= datetime.date.today()),

    # ======================================
    # ADDRESS VALIDATION
    # ======================================
    ("address", lambda person: isinstance(person["address"], dict) and len(person["address"]) > 0),

    # ======================================
    # PHONE_NUMBER VALIDATION
    # ======================================
    ("phone_number", lambda person: isinstance(person["phone_number"], str) and
                                    person["phone_number"].isdigit() and
                                    len(person["phone_number"]) == 8)
])
async def test_generate_person_key_properties(key, validator):
    # ACT
    result = await generate_person()

    # ASSERT
    assert key in result, f"Missing key '{key}' in person data"
    assert validator(result), f"Validation failed for key '{key}': {result[key]!r}"


# ===========================================================================================
# ADDRESS SUB-STRUCTURE TEST
# ===========================================================================================
async def test_generate_person_address_structure():
    # ACT
    person = await generate_person()
    address = person["address"]

    # ASSERT - Address should have expected structure
    assert isinstance(address, dict), "Address should be a dictionary"

    expected_address_fields = ["street", "number", "floor", "door", "postal_code", "town_name", "full_address"]
    for field in expected_address_fields:
        assert isinstance(address[field], str) and len(
            address[field]) > 0, f"Invalid address field {field}: {address[field]}"
