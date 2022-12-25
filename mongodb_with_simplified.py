
from pymongo import MongoClient

cluster = "mongodb+srv://<pass>:farzan@cluster0.fnc46cy.mongodb.net/mongodb_db?retryWrites=true&w=majority"
client = MongoClient(cluster)

client.list_database_names()
db = client.mongodb_db
collection = db.users
collection.insert_one({"name": "farzan", "age": 22})

