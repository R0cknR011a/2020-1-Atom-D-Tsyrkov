import pytest
from upgraded_list import MyList


def test_general():
    a = MyList(1, 2, 3)
    assert type(a) is MyList
    a.append(4)
    assert len(a) == 4
    a.pop()
    assert len(a) == 3


def test_addition_and_substraction():
    a = MyList(1, 2, 3)
    b = MyList(4, 5, 6, 7, 8, 9)

    assert a + b == MyList(5, 7, 9, 7, 8, 9)
    assert type(a + b) is MyList
    assert a == MyList(1, 2, 3)
    assert b == MyList(4, 5, 6, 7, 8, 9)

    assert a - b == MyList(-3, -3, -3, -7, -8, -9)
    assert type(a - b) is MyList
    assert a == MyList(1, 2, 3)
    assert b == MyList(4, 5, 6, 7, 8, 9)
    assert b + a == MyList(5, 7, 9, 7, 8, 9)

    assert type(b + a) is MyList
    assert a == MyList(1, 2, 3)
    assert b == MyList(4, 5, 6, 7, 8, 9)
    assert b == MyList(4, 5, 6, 7, 8, 9)

    assert b - a == MyList(3, 3, 3, 7, 8, 9)
    assert type(b - a) is MyList
    assert a == MyList(1, 2, 3)
    assert b == MyList(4, 5, 6, 7, 8, 9)

    a.append(4)
    a.append(5)
    a.append(6)

    assert a + b == MyList(5, 7, 9, 11, 13, 15)
    assert type(a + b) is MyList
    assert a == MyList(1, 2, 3, 4, 5, 6)
    assert b == MyList(4, 5, 6, 7, 8, 9)

    assert b + a == MyList(5, 7, 9, 11, 13, 15)
    assert type(b + a) is MyList
    assert a == MyList(1, 2, 3, 4, 5, 6)
    assert b == MyList(4, 5, 6, 7, 8, 9)

    assert a - b == MyList(-3, -3, -3, -3, -3, -3)
    assert type(a - b) is MyList
    assert a == MyList(1, 2, 3, 4, 5, 6)
    assert b == MyList(4, 5, 6, 7, 8, 9)

    assert b - a == MyList(3, 3, 3, 3, 3, 3)
    assert type(b - a) is MyList
    assert a == MyList(1, 2, 3, 4, 5, 6)
    assert b == MyList(4, 5, 6, 7, 8, 9)


def test_comparison():
    a = MyList(1, 2, 3)
    b = MyList(1, 2, 3)
    assert (a == b) is True

    a.append(4)
    assert (a >= b) is True
    assert (a == b) is False

    a.pop()
    assert (a >= b) is True
    assert (a <= b) is True
    assert (a == b) is True

    a.pop()
    assert (a <= b) is True
    assert (a < b) is True
    assert (a == b) is False
