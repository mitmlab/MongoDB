import hashlib
from jose import jwt
from fastapi import HTTPException
from database import users_collection

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"

# Password Hashing

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Generate JWT Token

def create_token(email):
    token = jwt.encode({"email": email}, SECRET_KEY, algorithm=ALGORITHM)
    return token

# Register User

def register_user(user):
    existing_user = users_collection.find_one({"email": user.email})

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")

    hashed_password = hash_password(user.password)

    user_data = {
        "name": user.name,
        "email": user.email,
        "password": hashed_password
    }

    users_collection.insert_one(user_data)

    return {"message": "User registered successfully"}

# Login User

def login_user(user):
    existing_user = users_collection.find_one({"email": user.email})

    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")

    hashed_password = hash_password(user.password)

    if hashed_password != existing_user["password"]:
        raise HTTPException(status_code=401, detail="Invalid password")

    token = create_token(user.email)

    return {
        "message": "Login successful",
        "token": token
    }

# Forgot Password

def forgot_password(data):
    existing_user = users_collection.find_one({"email": data.email})

    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")

    new_hashed_password = hash_password(data.new_password)

    users_collection.update_one(
        {"email": data.email},
        {"$set": {"password": new_hashed_password}}
    )

    return {"message": "Password updated successfully"}
