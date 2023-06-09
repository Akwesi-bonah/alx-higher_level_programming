#!/usr/bin/python3
"""Define  a Rectangle class"""


class Rectangle:
    """Represent a rectangle"""
    def __init__(self, width=0, height=0):
        """initial a new Rectangle
        Args:
            width: define the width of the rectangle
            height: define the height of the rectangle
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """find the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        a = self.__width * 2
        b = self.__height * 2

        return a + b
