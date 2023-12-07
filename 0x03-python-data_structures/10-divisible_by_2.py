#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newlist = my_list[:]
    count = 0
    for x in newlist:
        if x % 2 == 0:
            newlist[count] = True
            count += 1
        else:
            newlist[count] = False
            count += 1

    return newlist
