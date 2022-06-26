#!/usr/bin/python3

"""
function that prints a text with 2 new lines after each of these
characters: ., ? and :
"""


def text_indentation(text):
    """
    text must be a string, otherwise raise a TypeError exception
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    for i in ".?:":
        text = (i + "\n\n").join
        ([line.strip(" ") for line in text.split(i)])
    print("{}".format(text), end="")
