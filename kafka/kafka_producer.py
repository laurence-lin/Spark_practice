from kafka import KafkaClient, KafkaConsumer, KafkaProducer
import json
import time
import pandas as pd
import numpy as np

# Producer send data to topic
# Consumer receive data from topic


producer = KafkaProducer(
    bootstrap_servers=[
        'localhost:9092'
    ],  # clients must connect to bootstrap server before access kafka cluster
    value_serializer=lambda x: json.dumps(x).encode('utf-8'),  # Kafka accepts byte type
)

# Example: send json with number 1-1000 to topic
for i in range(1000):
    df = {"number": i}
    producer.send("numtest", value=df)
    time.sleep(3)

