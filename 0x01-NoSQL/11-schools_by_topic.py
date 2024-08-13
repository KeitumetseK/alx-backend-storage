#!/usr/bin/env python3
"""
Module to find schools by topic in a MongoDB collection.
"""

def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.
    
    :param mongo_collection: The MongoDB collection object.
    :param topic: The topic to search for.
    :return: List of schools with the specified topic.
    """
    return list(mongo_collection.find({ "topics": topic }))

