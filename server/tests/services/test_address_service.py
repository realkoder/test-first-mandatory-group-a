import pytest
from app.models.postal_code import PostalCode
from app.services.address_service import get_random_address
from tortoise.exceptions import ValidationError


# ===========================================================================================
# ADDRESS SERVICE INTEGRATION TEST
# ===========================================================================================
# This spec implements comprehensive testing strategies combining:
# - BLACK-BOX TESTING: Testing without knowledge of internal implementation
# - WHITE-BOX TESTING: Testing with knowledge of internal code structure
# ===========================================================================================


@pytest.mark.parametrize("key, validator", [
    # ======================================
    # STREET VALIDATIONS
    # ======================================
    ("street", lambda v: isinstance(v, str) and 1 <= len(v) <= 100),

    # ======================================
    # NUMBER VALIDATIONS
    # ======================================
    ("number", lambda v: v.isalnum() and 1 <= len(v) <= 4),

    # ======================================
    # NUMBER VALIDATIONS
    # ======================================
    ("floor", lambda v: v == "st" or (v.isalnum and 1 <= len(v) <= 2)),

    # ======================================
    # DOOR VALIDATIONS
    # ======================================
    ("door", lambda v: v in ["th", "mf", "tv", "number", "complex"] or 1 <= len(v) <= 50),

    # ======================================
    # POSTAL_CODE VALIDATIONS
    # ======================================
    ("postal_code", lambda v: v.isdigit() and len(v) == 4),

    # ======================================
    # TOWN_NAME VALIDATIONS
    # ======================================
    ("town_name", lambda v: isinstance(v, str) and 1 <= len(v) <= 100),
])
async def test_get_random_address_key_formats(key, validator):
    """
    Integration test verifying both presence and format constraints for each key.
    """
    result = await get_random_address()

    assert key in result, f"Missing key '{key}' in result"

    value = result[key]
    assert validator(value), f"Invalid format for key '{key}': {value!r}"


# ======================================
# STREET VALIDATIONS
# ======================================
async def test_get_random_address_for_postal_code_creation():
    # ACT
    result = await get_random_address()

    # ASSERT: Structure check
    assert "street" in result, "Missing 'street' key in result"


# ======================================
# NUMBER VALIDATIONS
# ======================================
async def test_get_random_address_for_street_name():
    # ACT
    result = await get_random_address()

    # ASSERT: Structure check
    assert "number" in result, "Missing 'number' key in result"


# ======================================
# FLOOR VALIDATIONS
# ======================================
async def test_get_random_address_for_floor_value():
    # ACT
    result = await get_random_address()

    # ASSERT: Structure check
    assert "floor" in result, "Missing 'floor' key in result"


# ======================================
# DOOR VALIDATIONS
# ======================================
async def test_get_random_address_for_door_value():
    # ACT
    result = await get_random_address()

    # ASSERT: Structure check
    assert "door" in result, "Missing 'door' key in result"


# ======================================
# POSTAL_CODE
# ======================================
async def test_get_random_address_for_postal_code():
    # ACT
    result = await get_random_address()

    # ASSERT: Structure check
    assert "postal_code" in result, "Missing 'postal_code' key in result"


# ======================================
# TOWN_NAME
# ======================================
async def test_get_random_address_for_town_name():
    # ACT
    result = await get_random_address()

    # ASSERT: Structure check
    assert "town_name" in result, "Missing 'town_name' key in result"


# ======================================
# NEGATIVE TESTS
# ======================================
async def test_raises_error_if_no_postal_codes():
    # ARRANGE & ACT
    await PostalCode.all().delete()

    # ASSERT
    with pytest.raises(ValueError, match="No postal codes available"):
        await get_random_address()
