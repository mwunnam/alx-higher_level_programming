#!/usr/bin/python3

def uppercase(str):
    new_str = ""
    for x in str:
        if 'a' <= x <= 'z':
            new_str += chr(ord(x) - 32)
        else:
            new_str += x 

    print(new_str)
