#!/usr/bin/python3
import json
""" Function that returns the JSON representation of an object"""


def to_json_string(my_obj):
    """ Function return the JOSON represtion of an object
    parameters:
    my_obj: Object to be converted
    Return: The JSON representation of the object
    """
    return json.dumps(my_obj)
