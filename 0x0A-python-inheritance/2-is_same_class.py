#!/usr/bin/python3
"""
This is a module container of the function 2-is_same_class
"""


def is_same_class(obj, a_class):
    """return true if obj is the exact class a_class, otherwise false"""
    return (type(obj) == a_class)
