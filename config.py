import os
from pymongo import MongoClient

# db_uri = os.environ.get("MONGO_URI")
mongo_client = MongoClient("mongo")['bits_scalable']['users']
