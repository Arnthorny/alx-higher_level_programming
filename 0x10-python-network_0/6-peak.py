#!/usr/bin/python3
"""
Script for a function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    This function uses a binary search method to determine
    a peak integer from the list.

    Args:
        (list): List of integers to find the peak from

    Return:
        (int|None): Returns the peak integer or `None` if  list is empty
    """
    if not list_of_integers:
        return
    elif len(list_of_integers) == 1 or len(list_of_integers) == 2:
        return max(list_of_integers)

    lo = list_of_integers
    le, ri = (0, len(lo))
    while True:
        mid = int(le + (ri - le)/2)
        if mid == le:
            return lo[mid]
        prev = lo[mid - 1] if mid > 0 else float('-inf')
        next = lo[mid + 1] if mid < len(lo) - 1 else float('-inf')
        curr = lo[mid]
        if curr > next and curr > prev:
            return lo[mid]
        elif prev >= curr:
            ri = mid
            continue
        elif curr <= next:
            le = mid
            continue
