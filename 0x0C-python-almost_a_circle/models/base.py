#!/usr/bin/python3
""" represent base class for the project"""
import json


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


if __name__ == "__main__":
    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)
