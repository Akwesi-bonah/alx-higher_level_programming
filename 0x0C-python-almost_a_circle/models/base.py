#!/usr/bin/python3
""" represent base class for the project"""
import json
import csv


class Base:
    """Define base class"""
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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Dictionary to JSON string"""
        if list_dictionaries is None \
                or list_dictionaries == []:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        JSON string to file
        Args:
            list_objs: list of instances who inherits
        """
        filename = cls.__name__ + '.json'

        with open(filename, 'w') as file:
            if list_objs is None:
                file.write('[]')
            else:
                list_dicts = [item.to_dictionary()
                              for item in list_objs]
                file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """JSON string to dictionary"""
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Dictionary to Instance"""
        if dictionary and dictionary != {}:
            new = None
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            elif cls.__name__ == "Square":
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """ File to instances"""
        filename = str(cls.__name__) + '.json'

        try:
            with open(filename, 'r') as file:
                list_dicts = Base.from_json_string(file.read())
                return [cls.create(**data) for data in list_dicts]
        except IOError:
            return []


    @staticmethod
    def load_from_file_from_csv(cls):
        """ File to instances to csv"""

        filename = str(cls.__name__) + ".csv"
        try:
            with open(filename, 'r') as file:
                if cls.__name__ == 'Rectangle':
                    names = ['id','width', 'height', 'x', 'y']
                if cls.__name__ == 'Square':
                    names = ['id', 'size', 'x','y']
                list_dicts = csv.DictReader(file, fieldnames=names)
                new_liat = [dict([key, int(value)]
                                 for key, value in data.items())
                            for data in list_dicts]
                return [cls.create(**data) for data in list_dicts]
        except IOError:
            return []



