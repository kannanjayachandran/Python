'''
    Testing linear Search using pytest
'''


from linear_Search import linearSearch


def test_1():
    assert linearSearch([x for x in range(100)], 99) == 99
    assert linearSearch([x for x in range(10)], 5) == 5


def test_2():
    assert linearSearch([1, 3, 5, 8, 3, 9, 0, 23], 5) == 2
    assert linearSearch([], 2) == -1
