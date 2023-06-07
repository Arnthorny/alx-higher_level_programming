#!/usr/bin/python3

for i in range(25, -1, -1):
    print(f"{chr(97+i)}" if i % 2 else f"{chr(65+i)}", end="")
