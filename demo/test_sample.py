# content of test_sample.py
def func(x):
    return x + 1

def test_correct_answer():
    assert func(3) == 4

def test_wrong_answer():
    assert func(2) == 4
