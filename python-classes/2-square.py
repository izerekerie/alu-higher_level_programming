#!/usr/bin/python3
"""no module to import"""


class Square:
    """Initializes a new instance of the Square class."""
    def __init__(self, size=0):
        """initializing an attribute to the object"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
