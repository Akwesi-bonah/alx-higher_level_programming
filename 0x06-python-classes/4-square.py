#!/usr/bin/python3

"""Define a class Square."""

class Square:

    def __init__(self, size=0):

         """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size >= 0:
            self.__size = size
        else:
            raise ValueError("size must be >= 0")

    def area(self):
         """Return the current area of the square."""
        return self.__size**2

    @property
    """Get/set the current size of the square."""
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value >= 0:
            self.__size = value
        else:
            raise ValueError("size must be >= 0")
