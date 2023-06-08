#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    aLen = len(argv) - 1
    print("{:d} ".format(aLen) +
          ("argument" if aLen == 1 else "arguments"), end='')
    print("." if aLen == 0 else ":")

    for i in range(aLen):
        print("{}: {}".format(i + 1, argv[i + 1]))
