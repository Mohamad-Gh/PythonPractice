from twttr import shorten

def test_name():
    assert shorten("name") == "nm"

def test_number():
    assert shorten("hEllo 00") == "hll 00"

def test_Capital():
    assert shorten("nAme") == "nm"

def test_punctuation():
    assert shorten("hEllo!") == "hll!"
