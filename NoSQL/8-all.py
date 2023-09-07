#!/usr/bin/env python3
"""
This code will list all docs in a mongodb collection
"""


def list_all(mongo_collection):
    """
    list all documents in a collection
    """
    return mongo_collection.find() or []


if __name__ == "__main__":
    list_all(mongo_collection)
