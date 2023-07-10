#!/usr/bin/python3
"""Represent square class that inherits from rectangle class"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """define square class"""

    def __init__(self, size):
        """initialize square class"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Returns string representation of the square"""

        string = f"[{str(__class__.__name__) }] "
        string += f"{str(self.__size)}/{self.__size}"
        return string


if __name__ == "__main__":
    s = Square(13)

    print(s)
    print(s.area())




