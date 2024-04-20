import pytest
from fuel import convert, gauge


def test_guage_E():
    assert gauge(1) == "E"

def test_guage_F():
    assert gauge(99) == "F"

def test_guage_number():
    assert gauge(20) == "20%"


def test_convert_str():
    with pytest.raises(ValueError):
        convert("cat")

def test_convert_zero():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")

def test_convert_default():
    assert convert("2/5") == 40

def test_convert_bigone():
    with pytest.raises(ValueError):
        convert("2/1")
