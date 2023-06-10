#!/usr/bin/python3
def max_integer(my_list=[]):
    l_list = len(my_list)
    if l_list == 0:
        return None
    else:
        maxVal = my_list[0]
        for num in my_list:
            if num > maxVal:
                maxVal = num
        return maxVal
