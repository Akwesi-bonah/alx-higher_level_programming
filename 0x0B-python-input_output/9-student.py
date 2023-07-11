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

    def to_json(self):
        """dictionary represent of the class"""
        return self.__dict__


if __name__ == "__main__":
    students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

    for student in students:
        j_student = student.to_json()
        print(type(j_student))
        print(j_student['first_name'])
        print(type(j_student['first_name']))
        print(j_student['age'])
        print(type(j_student['age']))
