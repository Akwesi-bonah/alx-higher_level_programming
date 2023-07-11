#!/usr/bin/python3
"""function that read a file"""


def read_file(filename=""):
    """define read file """
    with open(filename, 'r', encoding='UTF8') as file:
        for line in file:
            line = line.replace('\n', "")
            print(line)


if __name__ == "__main__":
    read_file("txt/my_file_0.txt")
