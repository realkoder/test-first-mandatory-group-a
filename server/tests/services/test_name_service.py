import pytest
from app.services.name_service import get_random_name_gender


# ===========================================================================================
# NAME SERVICE INTEGRATION TEST
# ===========================================================================================
@pytest.mark.parametrize("key, validator", [
    # ======================================
    # FIRST_NAME VALIDATIONS
    # ======================================
    ("first_name", lambda v: isinstance(v, str) and 1 <= len(v) <= 30),

    # ======================================
    # LAST_NAME VALIDATIONS
    # ======================================
    ("last_name", lambda v: isinstance(v, str) and 1 <= len(v) <= 30),

    # ======================================
    # GENDER VALIDATIONS
    # ======================================
    ("gender", lambda v: v == 'female' or v == 'male')
])
async def test_get_random_address_key_formats(key, validator):
    # ARRANGE
    result = await get_random_name_gender()

    # ASSERT
    assert key in result, f"Missing key '{key}' in result"

    value = result[key]
    assert validator(value), f"Invalid format for key '{key}': {value!r}"
