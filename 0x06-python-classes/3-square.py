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
