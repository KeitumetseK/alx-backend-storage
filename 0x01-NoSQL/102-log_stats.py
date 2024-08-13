from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
nginx_collection = client.logs.nginx

def log_stats():
    print(f"{nginx_collection.count_documents({})} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    status_count = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")

    print("IPs:")
    top_ips = nginx_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")

if __name__ == "__main__":
    log_stats()

