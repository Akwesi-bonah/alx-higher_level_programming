#!/usr/bin/python3
""" Represent a class Student that defines a student"""


class Student:
    """Represent student"""

    def __init__(self, first_name, last_name, age):
        """
        initialize the class
        Args:
            first_name:  student first name
            last_name:  student last name
            age: student age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary represent of the class"""
        if type(attrs) == list and\
                all(type(item) == str for item in attrs):
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json):
        """
         replaces all attributes of the Student instance
        Args:
            json: key value to replace the dictionary
        """

        for key, value in json.items():
            setattr(self, key, value)
