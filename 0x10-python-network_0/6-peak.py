#!/usr/bin/python3
"""function"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers."""
    lint = list_of_integers
    if lint:
        lint.sort()
        return lint[-1]
    else:
        return None
