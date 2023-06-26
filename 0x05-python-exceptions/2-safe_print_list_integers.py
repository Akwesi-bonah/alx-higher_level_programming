#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    len = 0
    for idx in range(x):
        try:
            print("{:d}".format(my_list[idx]), end="")
            len += 1
        except (ValueError, TypeError):
            pass
    print()
    return  len
