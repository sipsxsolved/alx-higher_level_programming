#!/usr/bin/python3
"""This module contains a Rectangle class that defines a rectangle"""


class Rectangle:
    """This class defines a rectangle object"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialization with optional width and height"""
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

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

    def area(self):
        """A function that returns the area of a rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """A function that returns the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """A function that prints a graphical repr of the rectangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join(str(self.print_symbol) * self.__width
                                for _ in range(self.__height))
        return string

    def __repr__(self):
        """A function that returns official str repr of the rectangle object"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        print("Bye rectangle...")
        self.__class__.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """A function that returns the begger rect based on area

        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of any of the args is
                not an instance of Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """A function that returns a new Rectangle
        instance with width == height == size"""
        return cls(size, size)
