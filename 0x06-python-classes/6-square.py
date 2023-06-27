#!/usr/bin/pyhton3
class Square:
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
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print("_" * self.__position[0] + "#" * self.__size)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
