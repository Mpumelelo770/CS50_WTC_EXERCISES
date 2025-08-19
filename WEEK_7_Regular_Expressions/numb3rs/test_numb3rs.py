

from numb3rs import validate


def test_4sections():
    assert validate("1.1.1.1") == True
    assert validate("1.2.3.4") == True
    assert validate("12.34.45.60") == True
    assert validate("123.250.74.300") == False
    assert validate("abc.123.@#$.xyz") == False
    assert validate("1234.4321.123.321") == False

def test_randim():
    assert validate("Mpumelelo") == False
    assert validate("0123456789") == False
    assert validate("!@#$%,") == False
    assert validate("ip adress") == False

def test_Nsections():
    assert validate("12.34.45") == False
    assert validate("123.321") == False
    assert validate("12345") == False
    assert validate("123.123.124.123.123") == False
