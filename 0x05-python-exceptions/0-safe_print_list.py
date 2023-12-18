#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    element_printed = 0

    try:
        for i in range(x):
            print(my_list[i], end="")
            element_printed += 1

    except IndexError:
        print("index dosen't exit")

    finally:
        print()

    return (element_printed)
