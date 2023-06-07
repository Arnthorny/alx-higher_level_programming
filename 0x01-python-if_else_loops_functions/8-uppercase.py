#!/usr/bin/python3
def uppercase(str):
    for c in str:
        cN = "{}".format(chr(ord(c) - 32)) \
             if (97 <= ord(c) < 123) else "{}".format(c)
        print(cN, end="")
    print()
