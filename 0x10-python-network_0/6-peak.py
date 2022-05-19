#!/usr/bin/python3
"""function"""


def find_peak(list_of_integers):

    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
