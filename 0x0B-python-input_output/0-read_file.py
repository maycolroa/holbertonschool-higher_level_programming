#!/usr/bin/python3
'''Reader'''


def read_file(filename=""):
    '''text file (UTF8)'''
    with open(filename, mode="r", encoding="utf-8") as f:
        my_file = f.read()
        print(my_file, end="")
