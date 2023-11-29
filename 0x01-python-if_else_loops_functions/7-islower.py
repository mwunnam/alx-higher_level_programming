#!/usr/bin/python3

def islower(c):
    if not c:
        return (False)
    for x in range(ord('a'), ord('z') + 1):
        if chr(x) == c:
            return (True)

    return (False)
