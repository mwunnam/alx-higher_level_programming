#!/usr/bin/python3
""" Function that returns the JSON representation of an object"""
import json

def to_json_string(my_obj):
    """ Function return the JOSON represtion of an object
    parameters:
    my_obj: Object to be converted
    Return: The JSON representation of the object
    """
    return json.dump(my_obj)
