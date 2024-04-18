from seasons import age_calculator
import pytest

def test_cal_deafult():
    assert age_calculator("1999-5-20") == "Twelve million, nine hundred seventy thousand eighty"

def test_faulty():
    with pytest.raises(SystemExit):
        age_calculator("19999")
