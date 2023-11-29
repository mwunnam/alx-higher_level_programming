#!/usr/bin/python3

for x in range(0, 9):
    for y in range(1 + x, 10):
        print("{}{}".format(x, y), end=", " if y < 9 or x < 8 else "")

print()
