#!/usr/bin/python3
"""if the object is exactly an instance of the specified class """


def is_same_class(obj, a_class):
    """Define is_same_class
    Args:
        obj : the object to check
        a_class: the class to  test
    Returns:
        True - if the object belong to the class
        False - if the object does not belong to the class

    """
    return type(obj) == a_class


if __name__ == "__main__":
    a = 1
    if is_same_class(a, int):
        print("{} is an instance of the class {}"
              .format(a, int.__name__))
    if is_same_class(a, float):
        print("{} is an instance of the class {}"
              .format(a, float.__name__))
    if is_same_class(a, object):
        print("{} is an instance of the class {}"
              .format(a, object.__name__))
