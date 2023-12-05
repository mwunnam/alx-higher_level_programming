#!/usr/bin/python3

import sys
if __name__ == "__main__":
    args = sys.argv
    count = len(args)
    result = 0

    for x in range(1, count):
        if args[x] == '-':
            result -= int(args[x])
        else:
            result += int(args[x])

    print("{}".format(result))
