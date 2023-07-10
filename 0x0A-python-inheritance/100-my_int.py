#!/usr/bin/python3
"""Represent a class that inherits from int class"""


class MyInt(int):
    """define a class MyInt"""

    def __eq__(self, value):
        """override the operator == with != """
        return self.real != value

    def __ne__(self, value):
        """override the operator != with =="""
        return self.real == value


if __name__ == "__main__":
    my_i = MyInt(3)
    print(my_i)
    print(my_i == 3)
    print(my_i != 3)
