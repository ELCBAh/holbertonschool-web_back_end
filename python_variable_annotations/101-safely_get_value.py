#!/usr/bin/env python3
"""
Given the parameters and the return values, add type annotations
to the function

def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
"""
from typing import Mapping, Any, Union, TypeVar, Dict


T = TypeVar('T')


def safely_get_value(
        dct: Mapping[Any, Any],
        key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    safely_get_value function that takes in 3 parameters:
    dct: a dictionary
    key: a key in the dictionary
    default: a default value
    """
    if key in dct:
        return dct[key]
    else:
        return default
