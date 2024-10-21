#!/usr/bin/python3
"""This module contains a Base class"""
import json


class Base:
    """This is a Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """The JSON string repr of a list of dicts"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file

        Args:
            cls: the class itself i.e the class
            that calls the method (since this is a classmethod)
            list_objs: list of objects
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string
        Args:
            json_string (str): string representing a list of dictionaries
        Returns:
            list of json string
        """
        a_list = []
        if json_string is not None and json_string != "":
            a_list = json.loads(json_string)
        return a_list

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        Args:
            dictionary (dict): dictionary
        Returns:
            an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances
        Returns:
            list of instances
        """
        filename = "{:s}.json".format(cls.__name__)

        try:
            with open(filename, mode="r", encoding="utf-8") as a_file:
                content_string = a_file.read()  # str of list of dictionaries
            a_list = cls.from_json_string(content_string)  # str to list
            list_instances = []
            for i in range(len(a_list)):  # a_list[i]: dictionary of attributes
                list_instances.append(cls.create(**a_list[i]))
        except:
            list_instances = []

        return list_instances
