#!/usr/bin/python3
"""
A function that adds 2 intergers
This function validates the type int or float
Otherwise, raise TypeError, Cast values too
Returns an interger: addition of a and b
"""


def add_integer(a, b=98):
    """
    Adds the input intergers
    """
    if (type(a) is float):
        a = int(a)
    if (type(b) is float):
        b = int(b)
    if not ((type(a) is int) or (type(a) is float)):
        raise TypeError('a must be an interger')
    if not ((type(b) is int) or (type(b) is float)):
        raise TypeError('b must be an interger')
    return (a + b)
