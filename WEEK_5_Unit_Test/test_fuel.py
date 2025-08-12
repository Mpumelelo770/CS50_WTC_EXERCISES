
import pytest     #to test for error handling
from fuel import convert, gauge


def test_convert_correct():
    assert convert("1/2") == 50
    assert convert("2/3") == 67
    assert convert("1/3") == 33
    assert convert("1/100") == 1
    assert convert("99/100") == 99


def test_valueError():
    with pytest.raises(ValueError):
        convert("3/2")
        convert("1.5/3")
        convert("1.5/4.5")
        convert("-1/3")
        convert("-2/-3")
        convert("1/-2")

def test_zeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")
        convert("100/0")


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(33) == "33%"
    assert gauge(50) == "50%"
    assert gauge(67) == "67%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"



