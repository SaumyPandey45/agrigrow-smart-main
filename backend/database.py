from pymongo import MongoClient

MONGO_URL = "mongodb://localhost:27017"
DB_NAME = "agrisoil"

client = MongoClient(MONGO_URL, serverSelectionTimeoutMS=5000)

try:
    client.server_info()
    print("MongoDB connected successfully")
except Exception as e:
    print("MongoDB connection failed:", e)

db = client[DB_NAME]

predictions_collection = db["predictions"]