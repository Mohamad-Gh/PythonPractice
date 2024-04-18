import pytest
from working import convert

def test_convert():
    assert convert ("9 AM to 10 AM") == "09:00 to 10:00"

def test_faulty_input():
    with pytest.raises(ValueError):
        convert ("10AM to 5 PM")

def test_faulty_time():
    with pytest.raises(ValueError):
        convert("10:70 AM to 5:61 PM")

def test_correct():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"


def test_PM_time():
    assert convert("5 AM to 5 PM") == "05:00 to 17:00"

def test_noTO():
    with pytest.raises(ValueError):
        convert("6 AM 7 PM")

