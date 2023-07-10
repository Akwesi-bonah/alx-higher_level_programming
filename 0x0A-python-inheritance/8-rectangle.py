#!/usr/bin/python3
"""Represent a class Rectangle that inherit from BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """define a rectangle based on basedGeometry"""

    def __init__(self, width, height):
        """
        Initialization of the rectangle
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height


if __name__ == "__main__":
    r = Rectangle(3, 5)

    print(r)
    print(dir(r))

    try:
        print("Rectangle: {} - {}".format(r.width, r.height))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r2 = Rectangle(4, True)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
