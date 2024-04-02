#!/usr/bin/python3
"""
This is a function that fines the hightest number within a list of intergers
"""


def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    peak = list_of_integers[0]

    for num in list_of_integers[1:]:
        if peak < num:
            peak = num
        else:
            peak
    return peak


if __name__ == "__main__":
