#!/usr/bin/python3
"""LockedClass class definition module"""


class LockedClass():
    """Restrict this class to have only 
    first_name attribute"""
    __slots__ = ('first_name')
