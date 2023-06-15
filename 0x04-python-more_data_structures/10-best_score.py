#!/usr/bin/python3

def best_score(a_dictionary, y=""):
    if a_dictionary:
        max_num = max(a_dictionary.values())

        max_num_ind = list(a_dictionary.values()).index(max_num)

        return (list(a_dictionary.keys())[max_num_ind])
    else:
        return None
