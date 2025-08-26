
from seasons import get_minutes
import pytest



def test_correct():
    assert get_minutes("2000-08-16") == "Thirteen million, one hundred fifty-seven thousand, two hundred eighty minutes"
    assert get_minutes("2000-01-01") == "Thirteen million, four hundred eighty-five thousand, six hundred minutes"
    assert get_minutes("2000-12-12") == "Twelve million, nine hundred eighty-seven thousand, three hundred sixty minutes"
    assert get_minutes("1999-06-06") == "Thirteen million, seven hundred eighty-six thousand, five hundred sixty minutes"
    assert get_minutes("2025-01-01") == "Three hundred thirty-five thousand, five hundred twenty minutes"

def test_invalid():
    with pytest.raises(ValueError):
        get_minutes("2000-12-32")
        get_minutes("2000-13-30")
        get_minutes("1999-15-60")
        get_minutes("05-05-2000")


def test_random():
    with pytest.raises(ValueError):
        get_minutes("Random")
        get_minutes("12345")
        get_minutes("birth date")
        get_minutes("@#$%")
