#!/usr/bin/python3

for i in range(10):
    for j in range(i + 1, 10):
        print(f"{i}", end="")
        if (i + 1) < 9:
            print(f"{j}", end=", ")
        else:
            print(f"{j}")
