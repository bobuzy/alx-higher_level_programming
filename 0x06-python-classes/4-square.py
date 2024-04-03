#!/usr/bin/python3
"""Module for square class definition"""


class Square:
    """Square class definition"""

    def __init__(self, size=0):
        """"Initialize attribute size"""

        self.__size = size

    @property
    def size(self):
        """Return the size of the square"""

        return size.__size

    @size.setter
    def size(self, value):
        """Define size value"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the square area"""

        area = self.__size ** 2
        return area
