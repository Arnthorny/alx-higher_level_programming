#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    sum_arg = 0
    aLen = len(argv) - 1

    for i in range(aLen):
        sum_arg += int(argv[i + 1])
    print(sum_arg)
