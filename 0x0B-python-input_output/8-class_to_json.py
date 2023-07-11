#!/usr/bin/python3
"""
Represent a function that returns the dictionary
description with simple data structure
(list, dictionary, string, integer and boolean)
 for JSON serialization of an object"""
import json


def class_to_json(obj):
    """return data structure
    (list, dictionary, string, integer and boolean)
     """
    return json.dumps(obj.__dict__)

