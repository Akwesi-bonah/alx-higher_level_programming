#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    roman_letters = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    result = 0
    prev_value = 0
    for char in range(len(roman_string) - 1, -1, -1):
        current_value = roman_letters[roman_string[char]]
        if current_value >= prev_value:
            result += current_value
        else:
            result -= current_value
        prev_value = current_value
    return result
