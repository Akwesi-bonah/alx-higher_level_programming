#!/usr/bin/python3
import sys

t_arg = len(sys.argv)
total = 0

if __name__ == "__main__":
    if t_arg > 1:
        for i in range(1, t_arg):
            total += int(sys.argv[i])
    print("{}".format(total))
