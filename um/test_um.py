from um import count

def test_default():
    assert count("um") == 1

def test_question():
    assert count(" um?") == 1

def test_many_um():
    assert count("Um? Mum? Is this that album where,"
                 " um, umm, the clumsy alums play drums?") == 2
def test_cs50():
    assert count("This is, um... CS50.") == 1


