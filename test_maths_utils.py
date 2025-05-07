from maths_utils import multiply

def test_multiply_positive_numbers():
    assert multiply(4, 5) == 20

def test_multiply_with_zero():
    assert multiply(0, 100) == 0

def test_multiply_negative_numbers():
    assert multiply(-3, 6) == -18
    assert multiply(-2, -7) == 14
