#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
from sys import argv

if (__name__ == "__main__"):
    aLen = len(argv) - 1

    if (aLen != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif (argv[2] not in "*+-/"):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]

    if (op == "+"):
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif (op == "-"):
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif(op == "*"):
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    else:
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
