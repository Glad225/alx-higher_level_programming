#!/usr/bin/python3
"""
This is a module container of the function 3-is_kind_of_class.py
"""


def is_kind_of_class(obj, a_class):
    """True if obj is an instance or inherited from a_class, else False"""
    return (isinstance(obj, a_class))
