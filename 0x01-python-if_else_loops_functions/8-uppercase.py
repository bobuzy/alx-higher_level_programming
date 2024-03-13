#!/usr/bin/python3
def uppercase(str):
    for aph in str:
        if ord('z') >= ord(aph) >= ord('a'):
            aph = chr(ord(aph)-32)
        print("{:s}".format(aph), end="")
    print()
