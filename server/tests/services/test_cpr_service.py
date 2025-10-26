
import datetime
import pytest
from app.services.cpr_service import generate_dob


# ======================================
# DOB Testing
# ======================================

def test_generate_dob_returns_date_and_string():
    dob_date, dob_ddmmyy = generate_dob()

    assert isinstance(dob_date, datetime.date), "dob_date return type should be datetime.date"
    assert isinstance(dob_ddmmyy, str), "dob_ddmmyy should be a string"
    assert len(dob_ddmmyy) == 6, "dob_ddmmyy has exactly 6 chars"
    assert dob_ddmmyy.isdigit(), "dob_ddmmyy string has only digits"


