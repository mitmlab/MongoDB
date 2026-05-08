from pymongo import MongoClient

# Step 1: Connect to local MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Step 2: Select database
db = client["new_database"]

# Step 3: Select collection
collection = db["students"]

# Step 4: Retrieve all documents
students = collection.find()

# Step 5: Print all documents
print("Students Data:\n")

for student in students:
    print(student)
