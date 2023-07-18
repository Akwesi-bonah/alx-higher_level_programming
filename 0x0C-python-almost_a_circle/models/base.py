#!/usr/bin/python3


""" represent base class for the project"""
import json


class Base:
    """
    Base model
    This Represents the "base" for all other classes in project 0x0C*.

    Private Class Attributes:
        __nb_object: Number of instantiated Bases

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialize base class
        Args:
            id: integer argument passed
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
