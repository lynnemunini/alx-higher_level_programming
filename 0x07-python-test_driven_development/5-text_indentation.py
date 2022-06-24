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
    for i in range(len(text)):
        print("{}".format(text[i]), end="")
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print()
            print()
