#!/usr/bin/python3
import json
from sys import argv
from os import path


def save_to_json_file(my_obj, filename):
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    with open(filename, encoding="utf-8") as file:
        return json.load(file)


if __name__ == "__main__":
    args = argv[1:]
    file_name = "add_item.json"

    if not path.exists(file_name):
        new_list = []

    else:
        new_list = load_from_json_file(file_name)

    new_list.extend(args)

    save_to_json_file(new_list, file_name)
