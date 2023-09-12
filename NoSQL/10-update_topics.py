#!/usr/bin/env python3
"""
This code will update a school document in the schools collection
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    returns updated school document
    """
    return mongo_collection.update_one(
        {"name": name}, {"$set": {"topics": topics}})
