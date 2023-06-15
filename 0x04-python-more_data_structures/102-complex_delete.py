#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    if not a_dictionary:
        return a_dictionary
    val_list = list(a_dictionary.values())

    if value not in val_list:
        return a_dictionary
    val_keys = list(a_dictionary)

    for key in val_keys:
        if a_dictionary[key] == value:
            a_dictionary.pop(key, "")
    return a_dictionary
