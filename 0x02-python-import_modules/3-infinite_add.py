#!/usr/bin/python3
import sys
def run():
    list_arguments = sys.argv
    add = 0
    for cnt in range(1, len(list_arguments)):
        add += int(list_arguments[cnt])
    print("{}".format(add))
if __name__ == "__main__":
    run()
