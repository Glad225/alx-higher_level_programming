#!/usr/bin/python3
"""
The lookup function container
"""


def lookup(obj):
    """returns a list of available attributes and methods of an object"""
    return dir(obj)
