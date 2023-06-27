#!/usr/bin/pyhton3


"""Define a class Square."""


class Square:
    """Initialize a new square.
        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
    def __init__(self, size=0, position=(0, 0)):

        if type(position[0]) and type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size >= 0:
            self.__size = size
        else:
            raise ValueError("size must be >= 0")
        self.__position = position

    def area(self):
        """Return the current area of the square."""
        return self.__size**2

    @property
    def size(self):
        """ Get/set the size of the sqaure"""
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
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    @property
    def position(self):
        """Get/set the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
