import json
import time
import random
from kafka import KafkaProducer

# Ubah port menjadi 9094 agar sesuai dengan jalur OUTSIDE di Docker
producer = KafkaProducer(
    bootstrap_servers=['localhost:9094'], 
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    # Tambahkan request_timeout agar tidak menunggu terlalu lama jika gagal
    request_timeout_ms=10000 
)
print("🚀 Mengirim data sensor ke Kafka...")

while True:
    data = {
        'item': random.choice(['Cola', 'Water', 'Coffee']),
        'price': random.choice([5000, 10000]),
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
    }
    producer.send('vending_data', data)
    print(f"Sent: {data}")
    time.sleep(2)