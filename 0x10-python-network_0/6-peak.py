#!/usr/bin/python3
"""contains the function find_peak"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
     if bool(list_of_integers) is False:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
