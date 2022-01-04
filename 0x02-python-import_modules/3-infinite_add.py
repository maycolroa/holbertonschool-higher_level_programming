#!/usr/bin/python3
import sys


def main():
    list_arguments = sys.argv
    sum = 0
    for count in range(1, len(list_arguments)):
        sum += int(list_arguments[count])
    print("{}".format(sum))


if __name__ == "__main__":
    main()
