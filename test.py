import pymongo
import certifi

client = pymongo.MongoClient("your_connection_string", tlsCAFile=certifi.where())
print(client.list_database_names())