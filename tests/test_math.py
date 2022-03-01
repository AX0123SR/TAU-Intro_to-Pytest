
import pytest

@pytest.mark.math
def test_one_plus_one():
    assert 1 + 1 == 2

@pytest.mark.math
def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c

def test_zero_division():

    with pytest.raises(ZeroDivisionError) as e:
        num = 1/0
    assert 'division by zero' in str(e.value)


# --------- A Paramterize Test Case ---------
products = [
    (1, 1, 2),
    (0, 0, 0),
    (-1, -1, -2),
    (1, -1, 0)
]

@pytest.mark.parametrize('a,b,add', products)
def test_addition(a, b, add):
    assert a + b == add



