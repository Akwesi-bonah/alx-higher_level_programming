#!/usr/bin/python
"""Represent a function that creates an
Object from a “JSON file """
import json


def load_from_json_file(filename):
    """
    Define Object from a JSON file
    Args:
        filename: file to load

    Returns: json file
    """

    with open(filename, 'r') as file:
        return json.load(file)
