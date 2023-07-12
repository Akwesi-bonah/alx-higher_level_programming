#!/usr/bin/python3
"""defines a function that add attribute object"""


def add_attribute(obj, att, value):
    """
    Add new attribute to the object
    Args:
        obj: object to be added to the attribute
        att: the name of the attribute
        value:  the value of the attribute

    Raises:
        TyperError: if the attribute cannot be added
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, att, value)
