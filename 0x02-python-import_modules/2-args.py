#!/usr/bin/python3
import sys
t_arg = len(sys.argv)

if __name__ == "__main__":
    print("{} arguments:".format(t_arg - 1))

    if t_arg > 1:
        for i in range(1, t_arg):
            print("{0}: {1}".format(i, sys.argv[i]))
