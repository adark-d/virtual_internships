# kafka_producer.py

import json
import random
import time
from datetime import datetime
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

scooters = [f"SCOOTER_{i:03d}" for i in range(1, 51)]

def generate_event():
    return {
        "scooter_id": random.choice(scooters),
        "timestamp": datetime.utcnow().isoformat(),
        "lat": round(random.uniform(48.85, 48.90), 6),
        "lon": round(random.uniform(2.34, 2.39), 6),
        "battery": round(random.uniform(10, 100), 2),
        "ride_status": random.choice(["start", "stop", "idle"])
    }

while True:
    message = generate_event()
    producer.send("zippy.paris.rides", value=message)
    print("Sent:", message)
    time.sleep(0.5)