from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")

# Create database
DB = client["authDB"]

# Create collection
users_collection = DB["users"]
