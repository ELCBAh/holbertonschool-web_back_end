#!/usr/bin/env python3
"""
This function returns the index range of a page.
"""


def index_range(page, page_size):
    """return index"""
    return (page - 1) * page_size, page * page_size
