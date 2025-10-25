import datetime
import pytest
from app.services.persons_service import generate_persons


# ===========================================================================================
# PERSONS SERVICE INTEGRATION TEST
# ==========================================================================================
@pytest.mark.parametrize("valid_count", [2, 5, 10, 50, 100])
async def test_generate_persons_valid_counts(valid_count):
    # ACT
    persons = await generate_persons(valid_count)

    # ASSERT
    assert isinstance(persons, list), "Should return a list"
    assert len(persons) == valid_count, f"Should generate exactly {valid_count} persons"

    # All persons should have valid structure
    for person in persons:
        required_keys = ["cpr", "first_name", "last_name", "gender", "dob", "address", "phone_number"]
        for key in required_keys:
            assert key in person, f"Missing key '{key}' in person"


@pytest.mark.parametrize("invalid_count", [0, 1, 101, 150, -5])
async def test_generate_persons_invalid_counts(invalid_count):
    # ACT & ASSERT
    with pytest.raises(ValueError, match="Count must be between 2 and 100"):
        await generate_persons(invalid_count)


async def test_generate_persons_data_consistency():
    # ACT
    persons = await generate_persons(10)

    # ASSERT
    for person in persons:
        # cpr validation
        assert len(person["cpr"]) == 11, f"Invalid CPR length: {person['cpr']}"
        assert person["cpr"][6] == "-", f"CPR missing hyphen: {person['cpr']}"

        # name validation
        assert 1 <= len(person["first_name"]) <= 30, f"Invalid first_name: {person['first_name']}"
        assert 1 <= len(person["last_name"]) <= 30, f"Invalid last_name: {person['last_name']}"

        # gender validation
        assert person["gender"] in ['female', 'male'], f"Invalid gender: {person['gender']}"

        # dob validation
        assert isinstance(person["dob"], datetime.date), f"DOB should be date object: {person['dob']}"
        assert person["dob"].year >= 1914, f"DOB before epoch: {person['dob']}"
        assert person["dob"] <= datetime.date.today(), f"DOB in future: {person['dob']}"

        # address validation
        assert isinstance(person["address"], dict), f"Address should be dict: {person['address']}"
        assert len(person["address"]) > 0, "Address should not be empty"

        # phone number validation
        assert len(person["phone_number"]) == 8, f"Invalid phone length: {person['phone_number']}"
        assert person["phone_number"].isdigit(), f"Phone should be digits: {person['phone_number']}"