#!/usr/bin/python3
"""represent a function that append to a file"""


def append_write(filename="", text=""):
    """
    Define append function
    Args:
        filename: file to append string
        text: text to append to the file
    """
    # count = 0
    with open(filename, 'a+', encoding="utf-8") as file:
        return file.write(text)

        # for _ in text:
        #     if _.isspace() or _ == '\n':
        #         count += 1
        #     count += 1
        # return count
