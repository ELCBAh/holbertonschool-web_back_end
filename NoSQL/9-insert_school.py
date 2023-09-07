#!/usr/bin/env python3
"""
This code will insert a new school into the schools collection
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    returns new school id
    """
    return mongo_collection.insert(kwargs)


if __name__ == '__main__':
    insert_school(mongo_collection, **kwargs)
