#!/usr/bin/python3
"""module definition for a Rectangle class"""


class Rectangle:
    """Rectangle class definition"""
    def __init__(self, width=0, height=0):
        """Initialize attributes

        Args:
            width: rectangel width
            height: rectangle height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of a Rectangle object"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width value
        Args:
            value: value of the width, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Retrieves the width of a Rectangle object"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height value
        Args:
            value: value of the height, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
