#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    l_weight = [x for _, x in my_list]
    l_weight_score = [x * y for x, y in my_list]
    return (float(sum(l_weight_score) / sum(l_weight)))
