import pytest
from suma import suma


def test_suma_positivos():
    assert suma(2, 3) == 5


def test_suma_negativos():
    assert suma(-2, -3) == -5