#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    for item in list(a_dictionary):
        if a_dictionary[item] == value:
            del a_dictionary[item]
    return a_dictionary
