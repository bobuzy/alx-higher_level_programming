#!/usr/bin/python3
"""module definition for a Rectangle class"""


class Rectangle:
    """Rectangle class definition"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize attributes

        Args:
            width: rectangel width
            height: rectangle height
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
                    rec_string += str(self.print_symbol)
                rec_string += '\n'
            return rec_string[:-1]
        return rec_string

    def __repr__(self):
        """return string rep of rectangle for production"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Delete a rectangle class instance"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Find and return the bigger Rectangle
        based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """return new Rectangle instance with width == height == size
        """
        return cls(size, size)
