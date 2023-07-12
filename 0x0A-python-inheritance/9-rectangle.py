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

    def area(self):
        """return the area of the rectangle"""

        return self.__height * self.__width

    def __str__(self):
        """String representation of rectangle class"""
        string = f"[{str(self.__class__.__name__)}] "
        string += f"{str(self.__width)}/{str(self.__height)}"
        return string


if __name__ == "__main__":
    r = Rectangle(3, 5)

    print(r)
    print(r.area())
