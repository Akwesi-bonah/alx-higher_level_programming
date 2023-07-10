#!/usr/bin/python3
"""checking for instance of object"""


def is_kind_of_class(obj, a_class):
    """
    function that returns True if the object is an instance of,
     or if the object is an instance of a class that inherited from, the specified class
    Args:
        obj : the object to check
        a_class: the class to  test

    Returns:
        True - if the object belong to the class
        False - if the object does not belong to the class

    """

    return isinstance(obj, a_class)


if __name__ == "__main__":

    a = 1
    if is_kind_of_class(a, int):
        print("{} comes from {}".format(a, int.__name__))
    if is_kind_of_class(a, float):
        print("{} comes from {}".format(a, float.__name__))
    if is_kind_of_class(a, object):
        print("{} comes from {}".format(a, object.__name__))