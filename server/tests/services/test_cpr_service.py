import re
import datetime
import pytest
from app.services.cpr_service import generate_dob, generate_cpr


# ======================================
# DOB Testing
# ======================================

def test_generate_dob_returns_date_and_string():
    dob_date, dob_ddmmyy = generate_dob()

    assert isinstance(dob_date, datetime.date), "dob_date type should be datetime.date"
    assert isinstance(dob_ddmmyy, str), "dob_ddmmyy should be a string"
    assert len(dob_ddmmyy) == 6, "dob_ddmmyy should have exactly 6 chars"
    assert dob_ddmmyy.isdigit(), "dob_ddmmyy string should only contain digits"


# ======================================
# CPR Testing
# ======================================

async def test_generate_cpr_returns_cpr_string_with_hyphen():
    result = await generate_cpr()
    cpr = result["cpr"]


    # Positive Testing
    assert isinstance(result, dict), "result should be a dict"
    assert "cpr" in result, "'CPR' key should be in result dict"

    assert isinstance(cpr, str), "cpr should be a string"
    assert len(cpr) == 11, "cpr string should be 11 chars including hyphen"

    # Negative Testing
    assert "name" not in result, "This function should not return 'Name' key"
    assert not isinstance(cpr, int), "CPR number variable should not be an integer"
    
    # And regex
    assert re.fullmatch(r"\d{6}-\d{4}", cpr), "cpr should be ddmmyy-xxxx"


async def test_generate_cpr_last_digit_match_gender(monkeypatch):
    fake_male = {"name": "Niels", "surname": "Bohr", "gender": "male"}
    fake_female = {"name": "Marie", "surname": "Curie", "gender": "female"}


    def fake_get_person_male():
        return fake_male

    def fake_get_person_female():
        return fake_female


    monkeypatch.setattr("app.services.cpr_service.get_person", fake_get_person_male)
    result_male = await generate_cpr()
    cpr_male = result_male["cpr"]

    monkeypatch.setattr("app.services.cpr_service.get_person", fake_get_person_female)
    result_female = await generate_cpr()
    cpr_female = result_female["cpr"]


    last_digit_male = int(cpr_male[-1])
    last_digit_female = int(cpr_female[-1])

    assert last_digit_male % 2 == 1, f"Expected male CPR to end with an odd digit, got {last_digit_male}"
    assert last_digit_female % 2 == 0, f"Expected female CPR to end with an even digit, got {last_digit_female}"


def test_generate_dob_string_matches_date():
    dob_date, dob_ddmmyy = generate_dob()

    day = int(dob_ddmmyy[:2])
    month = int(dob_ddmmyy[2:4])

    assert dob_date.day == int(day), "something"
    assert dob_date.month == int(month), "something"



def _test_generate_dob_day_and_month_bounds():
    # Without knowing the year, allow February up to 29
    dob_ddmmyy = generate_dob()

    dd = int(dob_ddmmyy[:2])
    mm = int(dob_ddmmyy[2:4])

    max_days = {
        1: 31, 2: 29, 3: 31,  4: 30,  5: 31,  6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    # Lower bounds
    assert dd >= 1, f"Day {dd} is below minimum"
    assert mm >= 1, f"Month {mm} is below minimum"

    # Upper bounds
    assert dd <= max_days[mm], f"Day {dd} invalid for month {mm}"
    assert mm <= 12, f"Month {mm} is above maximum value"

