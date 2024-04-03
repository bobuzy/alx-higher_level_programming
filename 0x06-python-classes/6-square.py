#!/usr/bin/python3
"""Module for square class definition"""


class Square:
    """Square class definition"""

    def __init__(self, size=0, position=(0, 0)):
        """"Initialize attribute size and position"""

        self.size = size
        self.position = position

    @property
    def size(self):
        """Property for size of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        """Define size value"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Property for position of square"""

        return self.__position

    @position.setter
    def position(self, value):
        """Define position value"""

        if (not isinstance(value, tuple) or len(value) != 2 or not
                all(isinstance(n, int) for n in value) or
                any(n < 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the square area"""

        area = self.__size ** 2
        return area

    def my_print(self):
        """Print a # square"""

        if self.__size == 0:
            print()
        else:
            for row in range(self.__position[1]):
                print()
            for column in range(self.__size):
                    print(" " * self.__position[0] + "#" * self.__size)
