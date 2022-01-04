#!/usr/bin/python3
import sys


def star():
    argc = len(sys.argv) - 1
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{:d} arguments:".format(argc))
        for count in range(1, argc + 1):
            print("{}: {}".format(count, sys.argv[count]))


if __name__ == "__main__":
    star()
