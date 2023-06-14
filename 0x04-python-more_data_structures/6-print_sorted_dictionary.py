#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    dic_key = sorted(list(a_dictionary.keys()))
    for key in dic_key:
        print(f'{key}: {a_dictionary[key]}')
