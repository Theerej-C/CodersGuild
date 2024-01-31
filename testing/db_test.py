import pymongo

database = pymongo.MongoClient("mongodb://localhost:27017/")

db = database["user_db"]

user_collection = db["user"]
# user_collection.drop()
user = user_collection.find()
c = user_collection.estimated_document_count()
print(c)
for n in user:
    print(n)