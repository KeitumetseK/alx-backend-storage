#!/usr/bin/env python3
"""
Script to provide statistics about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient

def log_stats():
    """Displays stats about Nginx logs stored in MongoDB."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    # Number of logs
    log_count = collection.count_documents({})
    print(f"{log_count} logs")

    # Method stats
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        method_count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    # Check for status path
    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    log_stats()

