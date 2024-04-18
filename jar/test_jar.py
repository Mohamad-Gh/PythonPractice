import pytest

from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(50)
    jar.deposit(11)
    assert jar.size == 11
    jar.deposit(20)
    assert jar.size == 31


def test_withdraw():
    jar = Jar(50, 37)
    jar.withdraw(5)
    assert jar.size == 32
    jar.withdraw(10)
    assert jar.size == 22
    jar.withdraw(12)
    assert jar.size == 10
    with pytest.raises(ValueError):
        jar.withdraw(11)