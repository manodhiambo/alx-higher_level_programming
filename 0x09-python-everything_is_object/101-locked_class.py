#!/usr/bin/python3
"""
Locked Class
"""


class LockedClass:
    """ Prevent user from creating new attributes """
    __slots__ = ['first_name']

    def __init__(self, first_n=""):
        self.first_name = first_n
