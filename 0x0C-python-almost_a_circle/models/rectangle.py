#!/usr/bin/python3
"""Represent rectangle the inherit base class"""
Base = __import__("base").Base

class Rectangle(Base):
    """define rectangle that inherit Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initialize rectangle class
        Args:
            width: width of the rectangle
            height: height of the rectangle
            x: x co-ordinate of the rectangle
            y: y co-ordinate of the rectangle
            id: id of the object
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if type(y) is not int:
            raise TypeError("width must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """get for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set value for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get value for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set value for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get value for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set value for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """Get value for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set value for y"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__y = value

