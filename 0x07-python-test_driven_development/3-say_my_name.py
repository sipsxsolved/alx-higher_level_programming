#!/usr/bin/python3
"""
Print string
"""
def say_my_name(first_name, last_name=""):
    """ print full name """
    if first_name and type(first_name) != str:
        raise TypeError('first_name must be a string')
    if last_name and type(last_name) != str:
        raise TypeError('last_name must be a string')
    print("My name is {} {}".format(first_name, last_name))
