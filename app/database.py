from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError, ConnectionFailure
from bson import ObjectId
from decouple import config


MONGO_URI = config('MONGO_URI')
MONGO_DB_NAME = config('MONGO_DB_NAME')

client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
db = client[MONGO_DB_NAME]


def connect_to_mongo():
    try:
        client.server_info()
        print("Connected to MongoDB!")
    except (ServerSelectionTimeoutError, ConnectionFailure):
        print("Unable to connect to MongoDB")


def close_mongo_connection():
    client.close()


def add_user(user):
    return db.users.insert_one(user)


def get_users():
    return [user for user in db.users.find()]


def get_user(user_id):
    return db.users.find_one({"_id": ObjectId(user_id)})


def update_user(user_id, user_data):
    db.users.update_one({"_id": ObjectId(user_id)}, {"$set": user_data})


def delete_user(user_id):
    db.users.delete_one({"_id": ObjectId(user_id)})

