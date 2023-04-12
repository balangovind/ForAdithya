from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()
client = MongoClient("mongodb://localhost:27017")
db = client["mydatabase"]
users_collection = db["users"]

@app.post("/users")
async def create_user(firstname: str, lastname: str, email: str):
    new_user = {"firstname": firstname, "lastname": lastname, "email": email}
    result = users_collection.insert_one(new_user)
    new_user["_id"] = str(result.inserted_id)
    return {"message": "User created successfully", "user": new_user}

@app.get("/users")
async def get_users():
    users = []
    for user in users_collection.find():
        user["_id"] = str(user["_id"])
        users.append(user)
    return {"users": users}

