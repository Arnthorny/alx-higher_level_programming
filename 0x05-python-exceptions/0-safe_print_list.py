#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elems_prntd = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end='')
            elems_prntd += 1
        print()
    except IndexError:
        print()
        return(elems_prntd)
    return(elems_prntd)
