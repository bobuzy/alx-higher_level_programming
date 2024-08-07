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

    def area(self):
        """Define and return rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Define and return rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """return string representative of a rectangle"""

        rec_string = ""

        if self.__height != 0 and self.__width != 0:
            for i in range(self.__height):
                for j in range(self.__width):
                    rec_string += '#'
                rec_string += '\n'
            return rec_string[:-1]
        return rec_string
