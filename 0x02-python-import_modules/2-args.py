#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("{} argument:".format(len(argv)))
    elif len(argv) == 0:
        print("{} arguments.".format(len(argv)))
    else:
        print("{} arguments:".format(len(argv)))
