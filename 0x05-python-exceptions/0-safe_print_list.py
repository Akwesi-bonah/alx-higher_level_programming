#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    len = 0
    for i in range(x):
        try:
            len += 1
            print(my_list[i], end='')
        except ValueError:
            len -= 1
            break
    print()
    return len
