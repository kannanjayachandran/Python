from binary_Search import binarySearch


def test_1():
    assert binarySearch([x for x in range(100)], 4) == 4
    assert binarySearch([x for x in range(10)], 100) == -1


def test_2():
    assert binarySearch([], 45) == -1
