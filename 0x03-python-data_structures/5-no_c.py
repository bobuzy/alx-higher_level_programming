#!/usr/bin/python3

def no_c(my_string):
    str = ""
    for abc in my_string:
        if abc != "c" and abc != "C":
            str += abc
    return str
