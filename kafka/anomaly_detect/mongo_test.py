from pymongo import MongoClient

client = MongoClient('localhost:27017')  # default mongo client address
collection = client.numtest.numtest

