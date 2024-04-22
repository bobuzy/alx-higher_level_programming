#!/usr/bin/python3
"""Square class definition module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class definition"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the Square instance using the Rectangle class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Print the basic information fo the square instance"""
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.width))

    @property
    def size(self):
        """Return the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Set the width and height attribute with a new value"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the attributes using args and kwargs"""
        if args:
            for ind in range(len(args)):
                if ind == 0:
                    self.id = args[ind]
                elif ind == 1:
                    self.size = args[ind]
                elif ind == 2:
                    self.x = args[ind]
                elif ind == 3:
                    self.y = args[ind]
                else:
                    raise TypeError("update() takes at most 4 arguments " +
                                    "but more than 4 was given")
        elif kwargs:
            self.id = kwargs.get('id', self.id)
            self.size = kwargs.get('size', self.width)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)

    def to_dictionary(self):
        """Return a dictionary representation of
        the Rectangle instance """
        square_dict = {"x": self.x, "y": self.y, "id": self.id,
                     "size": self.width}
        return(square_dict)
