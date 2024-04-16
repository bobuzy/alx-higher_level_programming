#!/usr/bin/python3
"""is_kind_of_class class definition module"""


def is_kind_of_class(obj, a_class):
    """check if obj is an instance of a_class
     or inheritance of a_class
    """
    return isinstance(obj, a_class)
