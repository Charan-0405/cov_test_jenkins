from calculator import add, subtract,multiply

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
def test_subtract():
    assert subtract(5 ,3) == 2
    assert subtract(0 ,4) == -4
    assert subtract(5 ,3) == 2
def test_multiply():
    assert multiply(5 ,3) == 15
    assert multiply(10 ,4) == 40