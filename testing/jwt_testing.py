import jwt
import pymongo
payload = jwt.decode("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYm95MjMiLCJleHAiOjE3MDYxOTg1NDEsImlhdCI6MTcwNjE5ODI0MX0.9MBJ5XGLALEVfzmvPu1kocynDXv_y4-VhWV5bdMXFJM", "django-insecure-)gv-#f0f_03fgvx)8mbb7w%_gtqgn44=3+#p@4*gq(y@i7!3ue", algorithms=['HS256'])
database = pymongo.MongoClient("mongodb://localhost:27017/")

db = database["user_db"]

user_collection = db["user"]
if user_collection.find_one({"user_name":payload["user_id"]}):
    print("Hello boy")
print(payload)