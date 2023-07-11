#!/usr/bin/python3
"""represent a function that write to a file"""


def write_file(filename="", text=""):
    """define a function that write a file"""
    count = 0
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

    for _ in text:
        if _.isspace() or _ == '\n':
            count+=1
        count +=1
    return count


if __name__ == "__main__":

    nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
    print(nb_characters)
