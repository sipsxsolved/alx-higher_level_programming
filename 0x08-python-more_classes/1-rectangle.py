#!/usr/bin/python3
"""This module contains a Rectangle class that defines a rectangle"""


class Rectangle:
    """This class defines a rectangle object"""
    def __init__(self, width=0, height=0):
        """Initialization with optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width property retriever"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Desc:
            Width property setter

        Args:
            value (int): The value to be set as the width

        Raises:
            TypeError: If value is not of class int
            ValueError: If width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height property retriever"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Desc:
            height property setter

        Args:
            value (int): The value to be set as the height

        Raises:
            TypeError: If value is not of class int
            ValueError: If height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
