# content of test_sample.py
def func(x):
    return x + 1

def func1(y):
    return y - 1

def test_correct_answer():
    assert func(3) == 4

def test_correct_answer1():
    assert func1(5) == 4