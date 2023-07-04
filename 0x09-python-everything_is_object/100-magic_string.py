#!/usr/bin/pythhon3
def magic_string():
    n = magic_string.__dict__.get('n', 0) + 1
    magic_string.__dict__['n'] = n
    return "BestSchool, " * (n - 1) + "BestSchool"