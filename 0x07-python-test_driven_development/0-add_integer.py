#!/usr/bin/python3
"""module definition for add_integer"""


def add_integer(a, b=98):

    """ Return the sum of a and b
    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(100.3, -2)
    98
    >>> add_integer("Ben", 10)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        a, b = map(int, (a, b))
        return a + b


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
