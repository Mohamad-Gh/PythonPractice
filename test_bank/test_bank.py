from bank import value


def test_deafult():
    assert value("hey") == 20

def test_number():
    assert value("20") == 100

def test_hello():
    assert value("hello") == 0

def test_Hello():
    assert value("Hello") == 0


