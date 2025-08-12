

from plates import is_valid


def test_length_one():
    assert is_valid("A") == False
    assert is_valid("B") == False
    assert is_valid("1") == False
    assert is_valid("#") == False

def test_length_two():
    assert is_valid("AB") == True
    assert is_valid("A1") == False
    assert is_valid("1A") == False
    assert is_valid("12") == False

def test_length_correct():
    assert is_valid("ABC123") == True
    assert is_valid("ABCD") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A1BC") == False
    assert is_valid("2ABCDE") == False
    assert is_valid("ABC012") == False
    assert is_valid("123456") == False
    assert is_valid("ABC12D") == False

def test_length_greater():
    assert is_valid("ABCD123") == False
    assert is_valid("ABCDEFG") == False
    assert is_valid("1234567") == False

def test_length_zero():
    assert is_valid("") == False

