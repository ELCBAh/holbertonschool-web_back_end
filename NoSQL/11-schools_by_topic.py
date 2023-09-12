#!/usr/bin/env python3
"""
This code will return the list of schools that are
in the collection that have certain topic
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    returns list
    """
    return mongo_collection.find({"topics": topic})
