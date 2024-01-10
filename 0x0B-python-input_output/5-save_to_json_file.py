#!/usr/bin/python3
""" Function that writes JSON file """


def save_to_json_file(my_obj, filename):
    """ Function that writeJSON

    parameters:
    filename: name of file
    my_obj: object to be written
    """
    import json

    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)
