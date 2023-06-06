#!/usr/bin/python3
for a in reversed(range(97, 123)):
    if a % 2 == 1:
        char = a - 32
    else:
        char = a
    print('{:c}'.format(char), end='')
