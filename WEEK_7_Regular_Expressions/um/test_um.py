
from um import count


def test_clean_um():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("um i need um") == 2
    assert count("um my name is ,um Mpumelelo um.") == 3

def test_cases_um():
    assert count("UM") == 1
    assert count("um") == 1
    assert count("Um") == 1
    assert count("uM") == 1
    assert count("Um i want UM some um icecream and Um coffee") == 4

def test_mixed_um():
    assert count("yummy") == 0
    assert count("pneumonoultramicroscopicsilicovolcanoconiosis") == 0
    assert count("uhm i need um something uM yummy") == 2
    assert count("Um, thanks for the album") == 1
