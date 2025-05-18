from pymongo import MongoClient
import certifi

uri = "mongodb+srv://bilalqwider:Bilal123@cluster0.ml9pvn7.mongodb.net/test?retryWrites=true&w=majority"

client = MongoClient(uri, tls=True, tlsCAFile=certifi.where())

try:
    client.admin.command('ping')
    print("Connected successfully to MongoDB Atlas!")
except Exception as e:
    print("Error:", e)
