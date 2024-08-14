#!/usr/bin/env python3
"""
Module to insert a new document in a MongoDB collection.
"""

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a MongoDB collection.
    
    :param mongo_collection: The MongoDB collection object.
    :param kwargs: Keyword arguments representing the document's fields.
    :return: The _id of the inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id

