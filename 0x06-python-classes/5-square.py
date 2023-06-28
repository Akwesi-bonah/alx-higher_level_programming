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
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Retuen the area the square"""
        return self.__size**2

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value >= 0:
            self.__size = value
        else:
            raise ValueError("size must be >= 0")

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print()

        for i in range(1, self.__size + 1):
            print("#" * self.__size)
