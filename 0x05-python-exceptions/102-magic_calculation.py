#!/usr/bin/python3

def magic_calaculation(a, b):
    result = 0
    for _ in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            result += a ** b / i
        except Exception as e:
            result = b + a
            break
        return result
