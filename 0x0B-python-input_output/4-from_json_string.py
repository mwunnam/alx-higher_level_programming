#!/usr/bin/python3
import json
""" Function that ther  JSON format of string to python """


def from_json_string(my_str):
    """ Function return JOSON format to python format
    parameters:
    my_str: Object to be converted
    Return: The converted joson to Python format
    """
    return json.loads(my_str)
