#!/usr/bin/python3


""" Define a square class """


class Square:

    """ Represent a square"""

    def __init__(self, size):
        """ Initialize new square instance
        Args:
            size (int): the size of the square
        """
        if size < 0:
            raise ValueError("")
        self.__size = size
