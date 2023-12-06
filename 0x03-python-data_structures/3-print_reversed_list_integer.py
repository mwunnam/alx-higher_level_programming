#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    lent = len(my_list)
    for x in range(lent, 0, -1):
        print("{}".format(x))
