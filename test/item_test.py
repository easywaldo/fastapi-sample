# content of test_sample.py
def func(x):
    return x + 1


def test_incorrect_answer():
    assert func(3) != 5


def test_correct_answer():
    assert func(4) == 5

def test_list_contains_value():
    list = ["hello world", "good bye", "python"]
    res = "python" in list
    assert res == True