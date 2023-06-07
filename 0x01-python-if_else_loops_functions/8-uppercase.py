#!/usr/bin/python3
def uppercase(str):
    for c in str:
        cN = f"{chr(ord(c) - 32)}" if (97 <= ord(c) < 123) else f"{c}"
        print(cN, end="")
    print()
