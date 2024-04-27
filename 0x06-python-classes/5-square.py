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
        self.__size = size

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

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print('#' * self.__size)
