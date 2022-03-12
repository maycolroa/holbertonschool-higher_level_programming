#!/usr/bin/python3
""" MyList Class """


class MyList(list):
    """class MyList"""
    def print_sorted(self):
        """prints the list"""
        print(sorted(self))
