from kafka import KafkaConsumer
from pymongo import MongoClient
import json, time


# Create consumer
consumer = KafkaConsumer(
    'numtest',  # subscribe topic
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',  # if consumer restart, it consumes from latest end of commit
    enable_auto_commit=True,  # enable commit after each interval
    group_id='my-group',  # consumer group name
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),  # deserialize bytes into json
)

client = MongoClient('localhost:27017')  # default mongo client address
collection = client.numtest.numtest  # Create database 'numtest' and collection 'numtest'

for message in consumer:  # iterate over consumer, listening to input
    message = message.value  # value in JSON format
    collection.insert_one(message)
    print('{} added to {}'.format(message, collection))

