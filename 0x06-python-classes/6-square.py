#!/usr/bin/python3
"""This module a module that define a class quare with attribute size."""


class Square:
    """
    Initialize a sqare instance.

    Raises:
        TypeError: if size is not an integer.
        ValueError: if size is less than 0.
    """

    def __init__(self, size=0, position=(0, 0)):
        """ Initialize a new square
            Args:
        size (int): The size of the square.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must >= 0")

        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not instance(value, tuple) or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive intergers')

        if not all(instance(i, int) for i in value):
            raise TypeError('position must be a tuple of 2 positive intergers')

        if value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive intergers')

        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return
        if self.__position[1] > 0:
            print("\n" * self.__position[1], end="")

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
