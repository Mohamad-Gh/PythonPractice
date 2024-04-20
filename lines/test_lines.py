
import pytest
from lines import input_check
from lines import lines_counter


def test_IC_deafult():
    assert input_check(["lines.py","hello.py"]) == True

def test_IC_notpy():
    with pytest.raises(SystemExit):
         input_check(["lines.py","hello"])

def test_IC_less():
    with pytest.raises(SystemExit):
         input_check(["hello.py"])

def test_IC_much():
    with pytest.raises(SystemExit):
         input_check(["1","hello.py","three"])

