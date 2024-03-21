#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = {}
    for new in a_dictionary:
        new_dict[new] = a_dictionary * 2
    return new_dict
