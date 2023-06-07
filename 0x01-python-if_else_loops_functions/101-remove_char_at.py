#!/usr/bin/python3
def remove_char_at(str, n):
    strCopy = ""
    for i in range(0, len(str)):
        if i != n:
            strCopy += str[i]
    return strCopy
