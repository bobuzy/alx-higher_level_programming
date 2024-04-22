#!/usr/bin/python3
"""Rectangle class definition module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class definition"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Return the Rectangle instance width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set a new width for instance object"""
        self.validate("width", value)
        self.__width = value

    @property
    def height(self):
        """Return the Rectangle instance height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set a new height for Rectangle instance"""
        self.validate("height", value)
        self.__height = value

    @property
    def x(self):
        """Return the Rectabgle instance x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set new x attribute for Rectangle instance"""
        self.validate("x", value)
        self.__x = value

    @property
    def y(self):
        """Return the Rectangle instance y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set new y attribute for Rectabgle instance"""
        self.validate("y", value)
        self.__y = value

    def validate(self, name, value):
        """Raise error if value is unacceptable"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if name in ("width", "height") and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if name in ("x", "y") and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """Return the area of the rectangle using the width and height"""
        return self.__width * self.__height

    def display(self):
        """Print too standard output the Rectangle using '#'"""
        for y_axis in range(self.__y):
            print()
        for row in range(self.__height):
            for x_axis in range(self.__x):
                print(" ", end="")
            for col in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Print the basic infprmation fo the rectangle class"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Update the attributes using args and kwargs"""
        if args:
            for ind in range(len(args)):
                if ind == 0:
                    self.id = args[ind]
                elif ind == 1:
                    self.__width = args[ind]
                elif ind == 2:
                    self.__height = args[ind]
                elif ind == 3:
                    self.__x = args[ind]
                elif ind == 4:
                    self.__y = args[ind]
                else:
                    raise TypeError("update() takes at most 5 arguments " +
                                    "but more than 5 was given")
        elif kwargs:
            self.id = kwargs.get('id', self.id)
            self.__width = kwargs.get('width', self.__width)
            self.__height = kwargs.get('height', self.__height)
            self.__x = kwargs.get('x', self.__x)
            self.__y = kwargs.get('y', self.__y)

    def to_dictionary(self):
        """Return a dictionary representation of
        the Rectangle instance """
        rec_dict = {"x": self.x, "y": self.y, "id": self.id,
                    "height": self.height, "width": self.width}
        return (rec_dict)
