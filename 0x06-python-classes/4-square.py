#!/usr/bin/python3
"""This module a module that define a class quare with attribute size."""


class Square():
    """
    Initialize a sqare instance.

    Args:
        size (int): The size of the square.

    Raises:
        TypeError: if size is not an integer.
        ValueError: if size is less than 0.
    """

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must >= 0")

        self.__size = value

    def area(self):
        return self.__size ** 2
