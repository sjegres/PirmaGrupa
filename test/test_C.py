import pytest
from src.uzdC import tmprtr as temp

def test_0():
    assert temp(0) == 273.15


def test_temp_poz():
    assert temp(5) == 278.15

def test_temp_neg():
    assert temp(-10) == 263.15