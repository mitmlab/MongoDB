#CREATE
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db = client["student_db"]

users = db["users"]

new_user = {"name":"Alice", "email":"alice@example.com", "age": 20}
result = users.insert_one(new_user)
print("Inserted ID: ", result.inserted_id)

many_user = [
    {"name":"Bob", "email" : "bob@example.com", "age": 22},
    {"name":"Carol", "email": "carol@example.com", "age": 19}
]
result = users.insert_many(many_user)
print("Inserted IDs: ", result.inserted_ids)

#READ
for user in users.find():
    print(user)

print("alice")
user = users.find_one({"name": "Alice"})
print(user)

results = users.find({"age" : {"$gt" : 20}})
for r in results:
    print(r["name"], r["age"])

#UPDATE
users.update_one(
    {"name": "Alice"},
    {"$set": {"age": 21}}   
)
print("Alice's age updated!")

users.update_many(
    {"age": {"$lt":21}},
    {"$set": {"status": "minor"}}
)

#DELTE
result = users.delete_one({"name" : "Alice"})
print("Delete count:", result.deleted_count)

result = users.delete_many({"status":"minor"})
print("Deleted: ", result.deleted_count, "users")

users.delete_many({})