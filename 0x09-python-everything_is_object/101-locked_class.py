#!/usr/bin/python3
"""Define a locked class"""


class LockedClass:
    """
    This class prevent creating new Locked attributes
    for the name 'first_name'.
    """
    __slots__ = ["first_name"]