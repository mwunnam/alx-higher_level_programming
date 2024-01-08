#!/usr/bin/python3
"""This module a module that define a class quare with attribute size."""


class Square:
    """
    Initialize a sqare instance.


    Raises:
        TypeError: if size is not an integer.
        ValueError: if size is less than 0.
    """

    def __init__(self, size=0):
        """ Initialize a new square
            Args:
        size (int): The size of the square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must >= 0")

        self.__size = size
