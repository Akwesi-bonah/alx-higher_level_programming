#!/usr/bin/python3
"""check if an object is an instance of a class"""


def inherits_from(obj, a_class):
    """
    define inherits to is an instance
    of a class that inherited
    Args:
        obj : the object to check
        a_class: the class to  test

    Returns:
        True - if the object belong to the class
        False - if the object does not belong to the class

    """

    return isinstance(obj, a_class) and type(obj) != a_class


if __name__ == "__main__":
    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))