#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for val in list(a_dictionary.keys()):
        if value == a_dictionary.get(val):
            del a_dictionary[val]
    return a_dictionary
