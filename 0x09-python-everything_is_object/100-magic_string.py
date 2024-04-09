#!/usr/bin/python3
def magic_string(repeat=[0]):
    repeat[0] = repeat[0] + 1
    return "BestSchool" + (", BestSchool" * (repeat[0] - 1))
