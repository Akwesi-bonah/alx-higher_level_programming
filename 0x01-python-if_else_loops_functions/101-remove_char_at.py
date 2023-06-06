#!/usr/bin/python3
def remove_char_at(str, n):
    if n > len(str) or n < 0:
        return (str)
    char = ""
    for a in range(len(str)):
        if a == n:
            char += ""
        else:
            char += str[a]
    return (char)
