#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) in range(97, 123):
            val = ord(i) - 32
            print(chr(val), end="")
        else:
            print(i, end="")

