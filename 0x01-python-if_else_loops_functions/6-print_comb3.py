#!/usr/bin/python3
for c in range(0, 9):
    for d in range(c + 1, 10):
        if c * 10 + d < 89:
            print("{:d}{:d}".format(c, d), end=", ")
print("{:d}".format(89))
