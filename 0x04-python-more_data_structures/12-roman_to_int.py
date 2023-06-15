#!/usr/bin/python3

def roman_to_int(roman_string):
    if(not(isinstance(roman_string, str))):
        return 0

    total = 0
    sLen = len(roman_string)
    dict_rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}

    for i in range(len(roman_string)):
        c_num = dict_rom.get(roman_string[i], 0)
        if (not c_num):
            return 0
        next_num = (dict_rom.get(roman_string[i + 1], 0)
                    if (i+1) < sLen else 0)
        if (c_num >= next_num):
            total += c_num
        else:
            total -= c_num
    return total
