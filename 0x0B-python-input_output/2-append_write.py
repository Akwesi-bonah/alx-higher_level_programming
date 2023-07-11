#!/usr/bin/python3
"""represent a function that append to a file"""


def append_write(filename="", text=""):
    """Define append function"""
    count = 0
    with open(filename, 'a+', encoding="utf-8") as file:
        file.write(text)

        for _ in text:
            if _.isspace() or _ == '\n':
                count += 1
            count += 1
        return count


if __name__ == "__main__":
    nb_characters_added = append_write("append_write.txt", "This School is so cool!\n")
    print(nb_characters_added)