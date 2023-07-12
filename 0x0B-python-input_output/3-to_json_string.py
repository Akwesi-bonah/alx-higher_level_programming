#!/usr/bin/python3
"""Represent json string"""
import json


def to_json_string(my_obj):
    """
    Define json to string
    Args:
        my_obj:  object to convert into json file
    """
    return json.dumps(my_obj)
