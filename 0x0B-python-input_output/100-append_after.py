#!/us/bin/pyhton3
"""Define a function to search and append
text if search string is found"""


def append_after(filename="", search_string="", new_string=""):
    """
    append text after each line containing searched
    string
    Args:
        filename: file to search for the string from
        search_string: text to find from the file
        new_string: text to append to the searched string
    """

    text = ""
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, 'w') as file:
        file.write(text)
