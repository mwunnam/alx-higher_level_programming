#!/usr/bin/python3
""" FUnction that adds integers """


def add_interger(a, b=98):
    """ Returns results of addition of thow integers a and b.

        Floats are accepted but will be typecasted into integers

        Raise error if any of the parameters is not a float of
        and integer
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be interger")

    return int(a) + int(b)
