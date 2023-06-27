#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    list_len_int = 0
    if not my_list:
        return list_len_int

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            list_len_int += 1
        except (ValueError, TypeError):
            pass
    if list_len_int:
        print()
    return(list_len_int)
