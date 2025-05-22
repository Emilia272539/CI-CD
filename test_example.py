# test_example.py
import pytest
import utils


@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (3, 4, 7)])
def test_add(a, b, expected):
    assert utils.add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(5, 2, 3), (10, 4, 6)])
def test_subtract(a, b, expected):
    assert utils.subtract(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(2, 3, 6), (4, 5, 20)])
def test_multiply(a, b, expected):
    assert utils.multiply(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(6, 3, 2.0), (10, 5, 2.0)])
def test_divide(a, b, expected):
    assert utils.divide(a, b) == expected
