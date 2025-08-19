

from working import validate_convert, convert
import pytest


def test_validate_convert():
    assert validate_convert(convert, "9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert validate_convert(convert, "9 AM to 5 PM") == "09:00 to 17:00"
    assert validate_convert(convert, "9:00 AM to 5 PM") == "09:00 to 17:00"
    assert validate_convert(convert, "9 AM to 5:00 PM") == "09:00 to 17:00"
    assert validate_convert(convert, "9:30 AM to 5:45 PM") == "09:30 to 17:45"
    assert validate_convert(convert, "9:05 PM to 5:10 AM") == "21:05 to 05:10"


def test_validate_convert_incorrect():
    with pytest.raises(ValueError):
        validate_convert(convert, "9:60 AM to 5:00 PM")
        validate_convert(convert, "9:00 AM to 5:60 PM")
        validate_convert(convert, "13:00 AM to 5:00 PM")
        validate_convert(convert, "9:00 AM to 13:00 PM")


def test_validate_convert_random():
    with pytest.raises(ValueError):
        validate_convert(convert, "12345")
        validate_convert(convert, "cat")
        validate_convert(convert, "abcABC123")
        validate_convert(convert, ",@#$")



