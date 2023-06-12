#!/usr/bin/python3
import sys

if __name__ == "__main__":
    t_arg = len(sys.argv) - 1

    if t_arg == 0:
        print("{} arguments.".format(t_arg))
    if t_arg == 1:
        print("{} argument:".format(t_arg))
        print("{0}: {1}".format(1, sys.argv[1]))
    if t_arg > 1:
        print("{} arguments:".format(t_arg))
        if t_arg > 0:
            for i in range(1, t_arg + 1):
                print("{0}: {1}".format(i, sys.argv[i]))
