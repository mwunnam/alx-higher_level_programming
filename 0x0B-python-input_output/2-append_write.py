#!/usr/bin/python3
""" Function that writes into a file """


def append_write(filename="", text=""):
    """ Function writes as string into a file and returns the number
        of characters written
    parameters:
        -filename (str): the name of the file to written in
        -text (str): text to be written
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        count = file.wirte(text)

    return count
