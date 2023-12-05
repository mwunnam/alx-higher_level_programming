#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = sys.argv
    count = len(args) - 1

    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("{} argument:".format(count))
        print("{}: {}".format(count, args[1]))

    else:
        print("{} arguments:".format(count))
        for x in range(count):
            print("{}: {}".format(x + 1, args[x + 1]))
