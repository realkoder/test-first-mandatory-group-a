import pytest
from app.models.postal_code import PostalCode
from app.services.address_service import get_random_address


# ===========================================================================================
# ADDRESS SERVICE INTEGRATION TEST
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
    # ARRANGE
    result = await get_random_address()

    # ASSERT
    assert key in result, f"Missing key '{key}' in result"

    value = result[key]
    assert validator(value), f"Invalid format for key '{key}': {value!r}"


# ======================================
# NEGATIVE TESTS
# ======================================
async def test_raises_error_if_no_postal_codes():
    # ARRANGE & ACT
    await PostalCode.all().delete()

    # ASSERT
    with pytest.raises(ValueError, match="No postal codes available"):
        await get_random_address()
