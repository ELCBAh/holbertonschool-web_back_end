#!/usr/bin/env python3
"""
type-annotated function sum_mixed_list
which takes a list mxd_lst of integers and floats
and returns their sum as a float.
"""


def sum_mixed_list(mxd_lst: list[int | float]) -> float:
    """
    Returns the sum of the list elements.
    """
    return sum(mxd_lst)