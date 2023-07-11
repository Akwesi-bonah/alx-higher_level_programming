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


if __name__ == "__main__":
    student_1 = Student("John", "Doe", 23)
    student_2 = Student("Bob", "Dylan", 27)

    j_student_1 = student_1.to_json()
    j_student_2 = student_2.to_json(['first_name', 'age'])
    j_student_3 = student_2.to_json(['middle_name', 'age'])

    print(j_student_1)
    print(j_student_2)
    print(j_student_3)
