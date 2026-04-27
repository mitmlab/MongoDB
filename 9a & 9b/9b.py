from pymongo import MongoClient

# Step 1: Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Step 2: Select database
db = client["new_database"]

# Step 3: Select collection
collection = db["students"]

# Step 4: Insert a new document
new_student = {
    "name": "Ram",
    "age": 28,
    "course": "Data science"
}

insert_result = collection.insert_one(new_student)

print("Inserted ID:", insert_result.inserted_id)

# Step 5: Retrieve the inserted document using its _id
retrieved_student = collection.find_one({"_id": insert_result.inserted_id})

# Step 6: Print the retrieved document
print("\nInserted Document:")
print(retrieved_student)
