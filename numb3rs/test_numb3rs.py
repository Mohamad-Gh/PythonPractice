from numb3rs import validate


def test_default():
    assert validate("4.4.4.4") == True

def test_faulty():
    assert validate("275.3.6.28") == False

def test_faulty():
    assert validate("255.255.255.255") == True

def test_str():
    assert validate("cat") == False



