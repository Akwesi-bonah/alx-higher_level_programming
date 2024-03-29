#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """ finds a peak in list of integers"""
    
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            # Move towards the higher side of the list
            left = mid + 1
        else:
            # Move towards the lower or equal side
            right = mid

    return list_of_integers[left]
