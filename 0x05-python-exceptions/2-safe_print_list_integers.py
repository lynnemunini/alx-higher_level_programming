#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        value = 0
        for i in my_list[:x]:
            if type(i) != int:
                pass
            else:
                print("{:d}".format(i), end="")
                value += 1
        print()
        return value
    except Exception:
        pass
