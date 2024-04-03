#!/usr/bin/python3
"""Module for square class definition"""


class Square:
    """Square class definition"""

    def __init__(self, size=0):
        """"Initialize attribute size"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the square area"""

        area = self.__size ** 2
        return area
