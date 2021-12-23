#!/usr/bin/python3
for count in range(ord('z'), ord('a') - 1, -1):
    if count % 2 == 1:
        count = count - 32
    print("{:s}".format(chr(count)), end="")
