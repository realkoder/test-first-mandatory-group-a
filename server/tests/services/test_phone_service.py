import pytest
from app.services.phone_service import generate_phone_number, VALID_PREFIXES


# ===========================================================================================
# PHONE SERVICE INTEGRATION TEST
# ===========================================================================================

@pytest.mark.parametrize("validator", [
    lambda v: isinstance(v, str),
    lambda v: len(v) == 8,
    lambda v: v.isdigit(),
    lambda v: any(v.startswith(prefix) for prefix in VALID_PREFIXES),
])
async def test_generate_phone_number_key_properties(validator):
    # ACT
    result = await generate_phone_number()

    # ASSERT
    assert validator(result), f"Validation failed for phone number: {result}"
