#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        value = 0
        for i in my_list[:x]:
            print("{}".format(i), end="")
            value += 1
        print()
        return value
    except Exception:
        print()
