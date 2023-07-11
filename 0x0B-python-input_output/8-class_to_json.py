#!/usr/bin/python3
"""
Represent a function that returns the dictionary
description with simple data structure
(list, dictionary, string, integer and boolean)
 for JSON serialization of an object"""
import json


def class_to_json(obj):
    """return data structure
    (list, dictionary, string, integer and boolean)
     """
    return obj.__dict__


if __name__ == "__main__":
    """ My class module
    """


    class MyClass:
        """ My class
        """

        def __init__(self, name):
            self.name = name
            self.number = 0

        def __str__(self):
            return "[MyClass] {} - {:d}".format(self.name, self.number)


    m = MyClass("John")
    m.number = 89
    print(type(m))
    print(m)

    mj = class_to_json(m)
    print(type(mj))
    print(mj)
