#!/usr/bin/python3
""" Function that ther  JSON format of string to python """


def from_json_string(my_str):
    """ Function return JSON format to python format
    parameters:
    my_str: Object to be converted
    Return: The converted json to Python format
    """
    import json

    return json.loads(my_str)
