import pytest
from app.models.postal_code import PostalCode
from tortoise.exceptions import ValidationError


# ===========================================================================================
# POSTAL_CODE MODEL UNIT_TEST
# ===========================================================================================
# This spec implements comprehensive testing strategies combining:
# - BLACK-BOX TESTING: Testing without knowledge of internal implementation
# - WHITE-BOX TESTING: Testing with knowledge of internal code structure
# ===========================================================================================


# ======================================
# POSTAL_CODE VALIDATIONS
# ======================================
@pytest.mark.parametrize(
    # ARRANGE
    'postal_code, should_be_valid, expected_error',
    [
        # Invalid postal_code partition 0 - 4
        ('', False, 'postal code must contain only numbers'),
        ('1', False, 'postal code must be exactly 4 digits'),  # +1 char
        ('10', False, 'postal code must be exactly 4 digits'),  # equivalence partition
        ('100', False, 'postal code must be exactly 4 digits'),  # -1 char from valid partition/boundary

        # Valid postal_code partition 4-4
        ('1000', True, None),

        # Invalid postal_code partition > 4
        ('10000', False, 'postal code must be exactly 4 digits'),  # +1 char
        ('1000000', False, 'postal code must be exactly 4 digits'),  # equivalence partition

        # Edge cases: unexpected data type, wrong postal_code format
        (None, False, 'postal_code is non nullable field, but null was passed'),
        (True, False, 'postal code must contain only numbers'),
        (10_000, False, 'postal code must be exactly 4 digits'),
        ('a', False, 'postal code must contain only numbers'),
        ('AFEIGIEn', False, 'postal code must contain only numbers'),
        ('#!e2', False, 'postal code must contain only numbers'),
        ('a12z', False, 'postal code must contain only numbers'),
        ('0000', True, None),
        ('9999', True, None),
    ]
)
async def test_postal_code_for_postal_code_creation(postal_code, should_be_valid, expected_error):
    if expected_error:
        # ACT
        with pytest.raises((ValidationError, ValueError)) as exc_info:
            await PostalCode.create(
                postal_code=postal_code,
                town_name='Test Town'
            )
        # ASSERT
        assert expected_error in str(exc_info.value).lower()
    else:
        # ACT
        created_postal_code = await PostalCode.create(
            postal_code=postal_code,
            town_name='Test Town'
        )
        # ASSERT
        assert created_postal_code.postal_code == postal_code


# ======================================
# TOWN_NAME VALIDATIONS
# ======================================
@pytest.mark.parametrize(
    # ARRANGE
    'town_name, should_be_valid, expected_error',
    [
        # Invalid town_name partition 0 - 3
        ('', False, 'town name cannot be empty'),  # invalid lower
        ('A', False, 'town name must be between 3 - 25 chars'),  # +1 char
        ('Aa', False, 'town name must be between 3 - 25 chars'),  # -1 char from valid partition/boundary

        # Valid town_name partition 3-25
        ('Lem', True, None),  # valid lower
        ('Asaa', True, None),  # +1 char
        ('Augustenborg', True, None),  # equivalence partition
        ('A' * 24, True, None),  # -1 char from valid upper
        ('A' * 25, True, None),  # valid upper

        # Invalid town_name partition > 25
        ('A' * 26, False, 'town name must be between 3 - 25 chars'),  # +1 char
        ('A' * 100, False, 'town name must be between 3 - 25 chars'),  # equivalence partition

        # Edge cases: unexpected data type, wrong town_name format
        (None, False, 'town_name is non nullable field, but null was passed'),
        (10_000, False, 'town name can only contain letters, spaces, hyphens, apostrophes, and dots'),
        ('#!e2', False, 'town name can only contain letters, spaces, hyphens, apostrophes, and dots'),
        ('a12z', False, 'town name can only contain letters, spaces, hyphens, apostrophes, and dots'),
        ('0000', False, 'town name can only contain letters, spaces, hyphens, apostrophes, and dots'),
        ('9999', True, 'town name can only contain letters, spaces, hyphens, apostrophes, and dots'),
    ]
)
async def test_postal_code_for_town_name_creation(town_name, should_be_valid, expected_error):
    if expected_error:
        # ACT
        with pytest.raises((ValidationError, ValueError)) as exc_info:
            await PostalCode.create(
                postal_code='1000',
                town_name=town_name
            )
        # ASSERT
        assert expected_error in str(exc_info.value).lower()
    else:
        # ACT
        created_postal_code = await PostalCode.create(
            postal_code='1000',
            town_name=town_name
        )
        # ASSERT
        assert created_postal_code.town_name == town_name
