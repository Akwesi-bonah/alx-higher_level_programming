#!/usr/bin/python3
"""represent a function that write to a file"""


def write_file(filename="", text=""):
    """
    write string to UTF_8 text file
    Args:
        filename: name of the file to write to
        text:  the to write in the file
    """
    # count = 0
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)

    # for _ in text:
    #     if _.isspace() or _ == '\n':
    #         count += 1
    #     count += 1
    # return count
