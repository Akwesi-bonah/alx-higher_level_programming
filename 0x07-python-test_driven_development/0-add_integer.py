#!/usr/bin/python3
"""Defines a function for integer Addition"""


def add_integer(a, b=98):
    """Return the sum of a and b

    Float arguments are type cast into integer

    Raises:
        TypeError: If a or b is not of int type or float
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
