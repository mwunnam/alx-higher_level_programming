#!/usr/bin/python3
""" Function that writes JSON file """


def load_from_json_file(filename):
    """ Function that writeJSON

    parameters:
    filename: name of file
    my_obj: object to be written
    """
    import json

    with open(filename, encoding="utf-8") as file:
        return json.load(file)
