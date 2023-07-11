#!/usr/bin/python3
"""function that read a file"""


def read_file(filename=""):
    """define read file """
    with open(filename, encoding='utf-8') as file:
        for line in file:
            line = line.replace('\n', "")
            print(line)


