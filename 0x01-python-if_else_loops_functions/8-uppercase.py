#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            result = ord(str[i]) - 32
        else:
            result = ord(str[i])
        print('{:c}'.format(result), end="")
    print()
