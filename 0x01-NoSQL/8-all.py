#!/usr/bin/env python3
"""
Module to list all documents in a MongoDB collection.
"""

def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.
    
    :param mongo_collection: The MongoDB collection object.
    :return: List of documents, or an empty list if none found.
    """
    return list(mongo_collection.find())

