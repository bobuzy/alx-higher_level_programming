#!/usr/bin/python3
"""is_same_class class definition module"""


def is_same_class(obj, a_class):
    """Check if the object is an instance of the specified class
    """
    return (type(obj) is a_class)
