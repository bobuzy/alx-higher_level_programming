#!/usr/bin/python3
"""class_to_json function definition module"""


def class_to_json(obj):
    """Return dictionary of the object"""
    return obj.__dict__
