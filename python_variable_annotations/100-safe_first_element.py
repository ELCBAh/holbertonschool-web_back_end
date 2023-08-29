#!/usr/bin/env python3
"""
Augment the following code with the correct duck-typed annotations:

# The types of the elements of the input are not know
def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None
"""
from typing import Union, Sequence, Any


def safe_first_element(list: Sequence[Any]) -> Union[Any, None]:
    """return typing elements"""
    if list:
        return list[0]
    else:
        return None
