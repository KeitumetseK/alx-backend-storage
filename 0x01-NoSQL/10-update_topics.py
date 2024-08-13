#!/usr/bin/env python3
"""
Module to update topics of a school in a MongoDB collection.
"""

def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of a school document based on its name.
    
    :param mongo_collection: The MongoDB collection object.
    :param name: The name of the school to update.
    :param topics: List of topics to set for the school.
    """
    mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )

