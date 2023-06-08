#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    for name in dir(hidden_4):
        if name[0] != '-' and name[1] != '-':
            print(name)
