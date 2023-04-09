#!/usr/bin/python3
# 101-locked_class.py

"""Defines alx locked class."""


class alx_LockedClass:
    """
    Prevent the user from instantiating new alx_LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
