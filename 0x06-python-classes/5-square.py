#!/usr/bin/python
class Square:

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size >= 0:
            self.__size = size
        else:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size**2

    @property
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

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(1, self.__size + 1):
            print("#" * self.__size)
