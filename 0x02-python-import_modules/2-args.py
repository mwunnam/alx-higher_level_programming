#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv
    count = len(args)

    if count > 1:
        for x in range(1, count):
            print("{}: {}".format(x, args[x]))
    else:
        print("0 arguments.")

    
