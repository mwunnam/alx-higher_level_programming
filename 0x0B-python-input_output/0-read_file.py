#!/usr/bin/python3
""" Defines a text reading funciton """


def read_file(filename=""):
    """ Read a text file (UTF9) and print its content of stdout

    parameters:
    filename (str): The name of the file to be read, Default is
                    empty strings
    Returns:
            None
    """

    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
