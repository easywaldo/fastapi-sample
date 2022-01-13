# content of test_sample.py
from typing import List, Sequence, TypeVar


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
    
T = TypeVar('T', int, float)
def vec2(x: T, y: T) -> List[T]:
    return [x, y]

def test_vec2():
    list = vec2(10, 5.5)
    assert list == [10, 5.5]