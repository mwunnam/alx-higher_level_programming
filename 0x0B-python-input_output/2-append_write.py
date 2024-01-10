#!/usr/bin/python3
""" Function that appends into a file """


def append_write(filename="", text=""):
    """ Function appens a string into a file and returns the number
        of characters written
    parameters:
        -filename (str): the name of the file to written in
        -text (str): text to be appended
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
