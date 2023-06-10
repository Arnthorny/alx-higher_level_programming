#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tp_a = [0, 0]
    for i in range(2):
        tp_a[i] = (0 if len(tuple_a) <= i else tuple_a[i]) +\
                (0 if len(tuple_b) <= i else tuple_b[i])
        new_tup = tuple(tp_a)
    return(new_tup)
