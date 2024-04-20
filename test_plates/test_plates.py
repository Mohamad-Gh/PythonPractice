from plates import is_valid

def test_high_count():
    assert is_valid("CSCSC0") == False

def test_letter_first():
    assert is_valid("05cs")== False

def test_number_inbetween():
    assert is_valid("cs50cs")== False

def test_puncuation():
    assert is_valid("CS,5.0")== False

def test_deafult():
    assert is_valid("CS50") == True

def test_alphabetical():
    assert is_valid("20") == False

def test_low_count():
    assert is_valid("OUTATIME") == False

def test_alph():
    assert is_valid("7ou") == False

