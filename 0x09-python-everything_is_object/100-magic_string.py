#!/usr/bin/python3
def magic_string(number=0):
    magic_string.number = getattr(magic_string, "number", 0) + 1
    return ("Holberton, " * magic_string.number)[:-2]
