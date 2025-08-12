

import pytest
from twttr import shorten



def test_upper():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("MPUMELELO") == "MPMLL"
    assert shorten("UPPER_CASE") == "PPR_CS"

def test_lower():
    assert shorten("twitter") == "twttr"
    assert shorten("mpumelelo") == "mpmll"
    assert shorten("lower_case") == "lwr_cs"

def test_mixed():
    assert shorten("Twitter") == "Twttr"
    assert shorten("Mpumelelo") == "Mpmll"
    assert shorten("Lower_Case") == "Lwr_Cs"

def test_digits():
    assert shorten("12345") == "12345"
    assert shorten("1000") == "1000"
    assert shorten("-12345") == "-12345"

def test_mixed():
    assert shorten("Abc,123") == "bc,123"
    assert shorten("@#$AeMp") == "@#$Mp"
    assert shorten("Hey_No_1") == "Hy_N_1"


