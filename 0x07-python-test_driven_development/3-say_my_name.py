#!/usr/bin/python3
"""Represent a name printing function"""


def say_my_name(first_name, last_name=""):
    """print a name

    Args:
        first_name: the first name to print
        last_name: the last name to print

    Raises:
            typeError: if first name or last name is not str
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":

    say_my_name("John", "Smith")
    say_my_name("Walter", "White")
    say_my_name("Bob")
    try:
        say_my_name(12, "White")
    except Exception as e:
        print(e)


class test:
    def __init__(self):
        pass

    def __repr__(self):
        pass