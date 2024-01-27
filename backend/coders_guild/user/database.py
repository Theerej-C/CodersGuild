import pymongo

database = pymongo.MongoClient("mongodb://localhost:27017/")

db = database["user_db"]

user_collection = db["user"]