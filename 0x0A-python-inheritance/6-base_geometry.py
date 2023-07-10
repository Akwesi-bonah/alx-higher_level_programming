#!/usr/bin/python3
"""Represent a class BaseGeometry"""


class BaseGeometry:
    """Define a class"""
    pass

    def area(self):
        """Define the area """
        raise Exception("area() is not implemented")


if __name__ == "__main__":

    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
