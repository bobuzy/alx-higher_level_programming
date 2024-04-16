#!/usr/bin/python3
"""BaseGeometry class definition module"""


class BaseGeometry:
    """Raise exception in area method"""

    def area(self):
        """Raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check validity of name and value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
