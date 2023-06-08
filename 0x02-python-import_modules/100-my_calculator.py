#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

count = len(sys.argv) - 1

if count != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

a = int(sys.argv[1])
b = int(sys.argv[3])
opr = sys.argv[2]
result = 0

if __name__ == "__main__":

    if opr == '+':
        result = add(a, b)
        print("{0} + {1} = {2}".format(a, b, result))
    elif opr == '-':
        result = sub(a, b)
        print("{0} - {1} = {2}".format(a, b, result))
    elif opr == '*':
        result = mul(a, b)
        print("{0} * {1} = {2}".format(a, b, result))
    elif opr == '/':
        result = div(a, b)
        print("{0} / {1} = {2}".format(a, b, result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
