#!/usr/bin/python3

def multiply_by_2(a_dictionary, key=""):
    if a_dictionary:
        new_dict = {x: val * 2 for x, val in a_dictionary.items()}
        return (new_dict)
