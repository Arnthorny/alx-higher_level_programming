#!/usr/bin/python3

def uniq_add(my_list=[]):
    if my_list:
        uniqL = set(my_list)
        return(sum(uniqL))
