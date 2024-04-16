#!/usr/bin/python3
"""Class definition module for Mylist"""


class MyList(list):
    """MyList class definition which
    Inherits the list class
    """

    def print_sorted(self):
        """Sorts and prints the list"""
        print(sorted(self))
