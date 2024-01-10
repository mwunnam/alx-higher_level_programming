#!/usr/bin/python3
""" Function that writes into a file """


def write_file(filename="", text=""):
    """ Function writes as string into a file and returns the number
        of characters written
    parameters:
        -filename (str): the name of the file to written in
        -text (str): text to be written
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        count = file.write(text)

    return count
