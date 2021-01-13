#!/usr/bin/python3
"""Slots"""


class LockedClass:
    """No object or class atribute"""

    __slots__ = ['first_name']

    def __init__(self, *args, **kwargs):
        """Initilization"""
        self.first_name = args
