#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):

    for j, k in sorted(a_dictionary.items()):
        print("{}: {}".format(j, k))
