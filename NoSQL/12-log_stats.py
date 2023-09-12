#!/usr/bin/env python3
"""
This code will count the number of logs in the database
and the number of logs for each method.
"""
import pymongo


if __name__ == "__main__":
    client = pymongo.MongoClient()
    db = client.logs
    collection = db.nginx
    print(f"{collection.count_documents({})} logs")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        print(f"{collection.count_documents({'\tmethod': method})} {method}")
    print(f"{collection.count_documents({'\tmethod': 'GET', 'path': '/status'})}\
        GET /status")
    client.close()
